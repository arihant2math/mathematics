from mathematics.algebra.term import Term


class Variable:
    def __init__(self, name: str, power=1):
        self.name = name
        self.power = power

    def __str__(self):
        return self.name + "^" + str(self.power)

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.power == other.power

    def __neg__(self):
        return Term({self}, -1)

    def __le__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name > other.name

    def __hash__(self):
        return hash(str(self))
