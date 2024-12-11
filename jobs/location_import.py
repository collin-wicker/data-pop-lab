from nautobot.apps.jobs import Job, register_jobs

class LocationImportJob(Job):
    """This job imports locations from a CSV file or CSV text input."""

    class Meta: 
        name = "Location Import Job"
        description = "This job imports locations from a CSV file or CSV text input."
    
    def run(self):
        """Do actions."""

register_jobs(LocationImportJob)