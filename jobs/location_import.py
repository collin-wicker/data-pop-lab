import csv
from io import TextIOWrapper

from nautobot.apps.jobs import FileVar, Job, register_jobs
from nautobot.dcim.models import Location, LocationType
from nautobot.extras.models import Status
from .state_abbreviations import STATE_ABBREVIATIONS

class LocationImportJob(Job):
    """This job imports locations from a CSV file or CSV text input."""

    csv_file = FileVar(
        label="CSV File",
        required=True,
        description="Provide the CSV file of locations to import."
    )

    class Meta: 
        name = "Location Import Job"
        description = "This job imports locations from a CSV file or CSV text input."
    
    def _find_state(self, state_abbr):
        state = STATE_ABBREVIATIONS.get(state_abbr)
        return state
    
    def _get_location_type(self, site_name):
        '''
        pass in the site name and return datacenter or branch
        :param site_name:
        :return: string
        '''
        if site_name.endswith("-DC"):
            #query NB data to get location Type UUID
            location_type = LocationType.objects.get(name="Data Center")
        if site_name.endswith("-BR"):
            location_type = LocationType.objects.get(name="Branch")
        if location_type:
            return location_type
        else:
            self.logger.error("Unable to find location type")

    def _process_csv_file(self, csv_file):
        """Convert CSV data into a dictionary containing Nautobot objects."""
        self.logger.info("Decoding CSV file...")
        with csv_file.open(mode="rb") as file:
            text_file = TextIOWrapper(file, encoding="utf-8")
            csv_reader = csv.DictReader(text_file)
            return csv_reader

    def run(self, csv_file):
        """Do actions."""
        # Process CSV data
        csv_data = self._process_csv_file(csv_file)
        # Get state, city, and active object types
        state_location_type = LocationType.objects.get(name="State")
        city_location_type = LocationType.objects.get(name="City")
        active_status_object = Status.objects.get(name="Active")

        for row in csv_data:
            if len(row["state"]) <= 2:
                state = self._find_state(row["state"])
            else:
                state = row["state"]
            #Get the state object, create if it doesn't exsist
            state_object, state_obj_created = Location.objects.get_or_create(
                name=state,
                defaults = {
                    "name": state,
                    "status":active_status_object,
                    "location_type": state_location_type
                }
            )
            # Get the city object, create if it doesn't exsist
            city_object, city_obj_created = Location.objects.get_or_create(
            name = row['city'],
            defaults = {
                "name": row['city'],
                "status": active_status_object,
                "parent":state_object,
                "location_type": city_location_type
                }
            )
            # Get location type based off of location name
            site_location_type = self._get_location_type(row['name'])
            site_object, site_object_created = Location.objects.get_or_create(
                name=row['name'],
                defaults = {
                    "name": row['name'],
                    "status": active_status_object,
                    "location_type": site_location_type,
                    "parent" : city_object
                }
            )
            if site_object_created:
                self.logger.info(f"Created the Following Entry - Site Name: {row['name']}, City: {row['city']}, State: {state}, Location Type: {site_location_type}")
            else:
                self.logger.info(f"Site: {row['name']} already Exists")

register_jobs(LocationImportJob)