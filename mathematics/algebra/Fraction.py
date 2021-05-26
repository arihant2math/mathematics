import math

from mathematics.algebra import Number


class Fraction:
    """A fraction class"""

    def __init__(self, s="", numerator=None, denominator=None):
        if (numerator is None) or (denominator is None):
            s = s.replace(" ", "")
            s = str(s).split("/")
            self.num = s[0]
            self.denominator = s[1]
        else:
            self.num = Number(numerator)
            self.denominator = Number(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        if int(denominator) > 0:
            self.denominator = denominator
        else:
            self.denominator = abs(denominator)
            self.num = -Number(self.num)

    def __str__(self):
        div_by = math.gcd(self.num, self.denominator)
        return str(self.num // div_by) + "/" + str(self.denominator // div_by)

    def __eq__(self, other):
        if (self.num == other.num) and (self.denominator == other.denominator):
            return True
        else:
            return False

    def __floor__(self):
        return self.num // self.denominator

    def __add__(self, other):
        the_lcm = math.lcm(self.denominator, other.denominator)
        self_denominator_lcm = the_lcm // self.denominator
        other_denominator_lcm = the_lcm // other.denominator
        return Fraction(numerator=((self.num * self_denominator_lcm) + (other.num * other_denominator_lcm)),
                        denominator=(the_lcm + the_lcm))

    def __sub__(self, other):
        the_lcm = math.lcm(self.denominator, other.denominator)
        self_denominator_lcm = the_lcm // self.denominator
        other_denominator_lcm = the_lcm // other.denominator
        return Fraction(((self.num * self_denominator_lcm) - (other.num * other_denominator_lcm)), (the_lcm + the_lcm))

    def __mul__(self, other):
        return Fraction(numerator=(self.num * other.num), denominator=(self.denominator * other.denominator))

    def __truediv__(self, other):
        return Fraction(numerator=(self.num * other.denominator), denominator=(self.denominator * other.num))

    def __floordiv__(self, other):
        return Fraction(
            numerator=(self.num * other.denominator), denominator=(self.denominator * other.num)).__floor__()

    def __bool__(self):
        return True

    def __pow__(self, power, modulo=None):
        return Fraction(numerator=Number(self.num ** power), denominator=Number(self.num ** power))

    def __abs__(self):
        return Fraction(numerator=abs(self.num), denominator=self.denominator)  # denominator will always be positive

    def simplify(self):
        """
        Simplifies the Fraction
        :return: Fraction
        """
        div_by = math.gcd(self.num, self.denominator)
        self.num //= div_by
        self.denominator //= div_by
        return Fraction(numerator=self.num, denominator=self.denominator)

    def __simplify(self):
        div_by = math.gcd(self.num, self.denominator)
        self.num //= div_by
        self.denominator //= div_by
        return Fraction(numerator=self.num, denominator=self.denominator)
