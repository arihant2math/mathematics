from fractions import Fraction

from mathematics.algebra.term import Term


class Variable:
    def __init__(self, name: str, power: Fraction):
        self.name = name
        self.power = power

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.power == other.power

    def __neg__(self) -> Term:
        return Term([self], -1)
