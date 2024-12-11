from nautobot.apps.jobs import FileVar, Job, register_jobs

class LocationImportJob(Job):
    """This job imports locations from a CSV file or CSV text input."""

    file_input = FileVar()

    class Meta: 
        name = "Location Import Job"
        description = "This job imports locations from a CSV file or CSV text input."
    
    def run(self):
        """Do actions."""
        pass

register_jobs(LocationImportJob)