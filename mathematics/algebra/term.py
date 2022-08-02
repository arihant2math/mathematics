from mathematics.algebra.variable import Variable


class Term:
    def __init__(self, variables, coefficient=1):
        self.variables = variables
        self.coefficient = coefficient

    def __mul__(self, other):
        if type(other) == int:
            return Term(self.variables, self.coefficient * other)
        elif type(other) == Variable:
            variables = self.variables
            variables.append(other)
            return Term(self.variables, self.coefficient)
