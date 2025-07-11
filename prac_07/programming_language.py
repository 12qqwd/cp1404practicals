class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return (
            f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
            f"Year={self.year}, PointerArithmetic={self.pointer_arithmetic}"
        )
