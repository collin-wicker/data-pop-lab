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
        decoded_csv_file = csv_file.read().decode("utf-8")
        print(decoded_csv_file)
        # csv_reader = csv.DictReader(StringIO(decoded_csv_file))
        # self.logger.info("Processing CSV data...")
        # processing_failed = False
        # processed_csv_data = {}

    
    def run(self, csv_file):
        """Do actions."""
        self._process_csv_file(csv_file)

register_jobs(LocationImportJob)