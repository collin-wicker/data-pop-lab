import csv
import logging
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

    def _process_csv_file(self, csv_file):
        """Convert CSV data into a dictionary containing Nautobot objects."""
        self.logger.info("Decoding CSV file...")
        with open(csv_file, "rb") as file:
            text_file = TextIOWrapper(file, encoding="utf-8")
            csv_reader = csv.DictReader(file)
            state_location_type = LocationType.objects.get(name="State")
            city_location_type = LocationType.objects.get(name="City")
            active_status_object = Status.objects.get(name="Active")

            for row in csv_reader:
                print(row["name"])
                print(row["city"])
                print(row["state"])


    
    def run(self, csv_file):
        """Do actions."""
        self._process_csv_file(csv_file)

register_jobs(LocationImportJob)