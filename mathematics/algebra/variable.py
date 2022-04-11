class Variable:
    """Emulates a Variable"""

    def __init__(self, var):
        self.name = ""
        self.coefficient = 1
        for char in var:
            if char.isalpha():
                if self.name != "":
                    raise ValueError("Invalid variable name, must be one letter")
                self.name = char

        if var - self.name == "":
            self.coefficient = 1
        else:
            self.coefficient = int(var - self.name)

    def __str__(self):
        if self.coefficient == 1:
            return self.name
        else:
            return str(self.coefficient) + self.name

    def __add__(self, other):
        if isinstance(other, Variable):
            if self.name == other.name:
                return Variable(str(self.coefficient + other.coefficient) + self.name)
            else:
                raise ValueError("Cannot add variables with different names")

    def __sub__(self, other):
        if isinstance(other, Variable):
            if self.name == other.name:
                return Variable(str(self.coefficient - other.coefficient) + self.name)
            else:
                raise ValueError("Cannot subtract variables with different names")

    def __abs__(self):
        return Variable(str(abs(self.coefficient)) + self.name)
