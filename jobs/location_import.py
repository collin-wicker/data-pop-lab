import csv

from nautobot.apps.jobs import FileVar, Job, register_jobs

class LocationImportJob(Job):
    """This job imports locations from a CSV file or CSV text input."""

    file_input = FileVar()

    class Meta: 
        name = "Location Import Job"
        description = "This job imports locations from a CSV file or CSV text input."
    
    def run(self, file_input):
        """Do actions."""
        # Open the CSV file
        with open(file_input, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                print(row)

register_jobs(LocationImportJob)