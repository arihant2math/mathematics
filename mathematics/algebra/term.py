class Term:
    def __init__(self, variables: list, coefficient: float):
        self.variables = variables
        self.variables.sort()
        self.coefficient = coefficient
        self._simplify()

    def __str__(self) -> str:
        return str(self.coefficient) + "".join(self.variables)

    def __eq__(self, other) -> bool:
        return (self.coefficient == other.coefficient) and (
                self.variables == other.variables
        )

    def __mul__(self, other):
        if type(other) is Term:
            v = self.variables
            v.extend(other.variables)
            return Term(v, self.coefficient * other.coefficient)
        elif type(other) is int or type(other) is float:
            return Term(self.variables, self.coefficient * other)

    def __neg__(self):
        return Term(self.variables, -self.coefficient)

    def _simplify(self):
        new_variable_list = []
        for variable in self.variables:
            for count, item in enumerate(new_variable_list):
                pass
        # self.variables = new_variable_list
