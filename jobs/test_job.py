from nautobot.apps.jobs import Job, ObjectVar

class ExampleJob(Job):
    """This is our example Job definition."""

    device = ObjectVar(
        model=Device,
        query_params={
            'status': 'Active'
        }
    )

    class Meta:
        name = "Example Job"
        description = "This is the description of my ExampleJob."
    
    def run(self, device):
        """Do all the things here."""
        if not device.manufacture.name == "Cisco":
            logger.warning("This object is not made by Cisco.", extra={"grouping": "validation", "object": device})
            raise Exception("A non Cisco device was selected.")