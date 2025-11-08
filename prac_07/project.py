class Project:
    """Represent a project object with name, start date, priority, cost estimte, completion percentage"""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0.0):
        """Initialise a project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a formatted string of project"""
        return f"{self.name}, start: {self.start_date}, Priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
