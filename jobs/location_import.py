import csv
import logging
from io import StringIO

from nautobot.apps.jobs import FileVar, Job, register_jobs

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
    
    def _process_csv_file(self, csv_file):
        """Convert CSV data into a dictionary containing Nautobot objects."""
        self.logger.info("Decoding CSV file...")
        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row.get("name")
                print(name)
                city = row.get("city")
                print(city)
                state = row.get("state")
                print(state)
        # text_file = csv_file.read().decode("utf-8")
        # for row in decoded_csv_file:
        #     print(row)

    
    def run(self, csv_file):
        """Do actions."""
        self._process_csv_file(csv_file)

register_jobs(LocationImportJob)