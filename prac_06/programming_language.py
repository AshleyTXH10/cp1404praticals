"""
Programming language
Estimate: 20 minutes
Actual:
"""

class ProgrammingLanguage():
    def __init__(self, name="", typing="", reflection=False, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.programming_language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"