class Expression:
    def __init__(self, terms):
        self.terms = terms
        self.simplify()

    def __add__(self, other):
        if type(other) is Expression:
            r = self.terms
            r.extend(other.terms)  # add the other expression's terms
            return r

    def simplify(self):
        pass
