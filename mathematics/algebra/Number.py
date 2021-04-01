"""Number Class"""


class Number(int):
    """The int class with extra features"""

    def __init__(self, num):
        super().__init__()
        self.num = num

    def __or__(self, sec_num):
        if (sec_num / self.num) % 1 == 0:
            return True
        else:
            return False

    def __pow__(self, power, modulo=None):
        if (type(power) == int) or (type(power) == Number):
            return Number(self.num ** power)
        elif type(power) == "Fraction":
            return (self.num ** power.num) ** (1.0 / float(power.denominator))
        else:
            raise TypeError

    def digit_sum(self):
        """Returns the sum of all the digits"""
        str_num = str(self.num)
        ans = Number(0)
        for item in str_num:
            ans += Number(item)
        return ans

    def digit_product(self):
        """Returns the sum of all the digits"""
        str_num = str(self.num)
        ans = Number(1)
        for item in str_num:
            ans *= Number(item)
        return ans
