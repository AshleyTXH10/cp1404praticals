CURRENT_YEAR = 2025
VINTAGE_REQUIREMENT = 50
class Guitar:
    """Make a guitar object with a name, year and cost"""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted guitar string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get current age of the guitar in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return if a guitar is vintage based on its age"""
        return self.get_age() >= VINTAGE_REQUIREMENT

    def __lt__(self, other):
        """Compare if guitar was made before another guitar"""
        return self.year < other.year