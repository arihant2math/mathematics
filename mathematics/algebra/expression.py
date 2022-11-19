from mathematics.algebra.term import Term


class Expression:
    def __init__(self, terms: list[Term]):
        self.terms = terms.sort()

    def __add__(self, other):
        if type(other) is Term:
            terms = self.terms
            terms.append(other)
            return Expression(terms)

    def __sub__(self, other):
        if type(other) is Term:
            terms = self.terms
            terms.append(other.__neg__)
            return Expression(terms)
