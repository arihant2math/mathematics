class NotPrimeException(Exception):
    def __init__(self):
        super().__init__("Number is not Prime")


class Number:
    def __init__(self, num):
        self.num = num
        print("Number constructor")


class Prime(Number):
    def __init__(self, num):
        fact = 1
        for i in range(1, num):
            fact = fact * i
        if fact % num != -1:
            raise NotPrimeException()
        super().__init__(num)
        print("Prime constructor")


class Merrsene(Prime):
    def __init__(self, num):
        super().__init__(num)


class SofieGermain(Prime):
    def __init__(self, num):
        super().__init__(num)
