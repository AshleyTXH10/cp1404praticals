class Band:
    """Band class for storing details of a band"""
    def __init__(self, name=""):
        """Construct a band with a name and 0 musicians."""
        self.musicians = []
        self.name = name

    def __str__(self):
        """Return a string representation of a band"""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string describing musicians and their instruments in a band"""
        lines = []
        for musician in self.musicians:
            if musician.instruments:
                lines.append(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                lines.append(f"{musician.name} needs an instrument!")
        return "\n".join(lines)