from mathematics.algebra.term import Term


class Variable:
    """Emulates a Variable"""

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if type(other) == Variable:
            return Term([self, other])
        elif type(other) == int:
            return Term([self], other)
        elif type(other) == Term:
            return other * self
