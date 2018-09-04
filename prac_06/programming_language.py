class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        if self.is_dynamic():
            typing = "Dynamic Typing"
        else:
            typing = "Static Typing"
        return "{}, {}, Reflection = {}, First appeared in {}".format(self.name, typing, self.reflection, self.year)
