from nautobot.apps.jobs import Job
from nautobot.extras.jobs import FileVar

class LocationImportJob(Job):
    """This job imports locations from a CSV file or CSV text input."""

    file_input = FileVar()

    class Meta: 
        name = "Location Import Job"
        description = "This job imports locations from a CSV file or CSV text input."
    
