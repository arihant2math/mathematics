"""Contains the Imaginary Number Class"""
from mathematics.algebra.Number import Number


class Imaginary:
    """
    emulates an imaginary number.
    """

    def __init__(self, num):
        num = str(num).lower().replace(" ", "")
        num = num.split("+")
        if len(num) == 1:
            self.imaginary_part = 0
            if "i" not in num[0]:
                self.real_part = Number(num[0])
                self.imaginary_part = 0
            else:
                self.real_part = 0
                self.imaginary_part = Number((num[0]).replace("i", ""))
        elif "i" in num[0]:
            self.imaginary_part = Number((num[0]).replace("i", ""))
            self.real_part = Number(num[1])
        elif "i" in num[1]:
            self.imaginary_part = Number((num[1]).replace("i", ""))
            self.real_part = Number(num[0])

    def __str__(self):
        return str(self.real_part) + "+" + str(self.imaginary_part) + "i"

    def __eq__(self, other):
        return (self.real_part == other.real_part) and (self.imaginary_part == other.imaginary_part)

    def __add__(self, other):
        real = int(self.real_part) + int(other.real_part)
        imaginary = int(self.imaginary_part) + int(other.imaginary_part)
        ans = str(imaginary) + "i" + "+" + str(real)
        return Imaginary(ans)

    def __sub__(self, other):
        real = int(self.real_part) - int(other.real_part)
        imaginary = int(self.imaginary_part) - int(other.imaginary_part)
        ans = str(imaginary) + "i" + "+" + str(real)
        return Imaginary(ans)

    def __mul__(self, other):
        real = (self.real_part * other.real_part) - (
                self.imaginary_part * other.imaginary_part
        )
        imaginary = (self.imaginary_part * other.real_part) + (
                self.real_part * other.imaginary_part
        )
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __truediv__(self, other):
        real = (self.real_part / other.real_part) - (
                self.imaginary_part / other.real_part
        )
        imaginary = (self.imaginary_part / other.real_part) + (
                self.real_part / other.imaginary_part
        )
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __floordiv__(self, other):
        real = (self.real_part // other.real_part) - (
                self.imaginary_part // other.real_part
        )
        imaginary = (self.imaginary_part // other.real_part) + (
                self.real_part // other.imaginary_part
        )
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __pow__(self, power: int, modulo=None):
        ans = self
        for i in range(power):
            ans = ans * self
        return Imaginary(ans)

    def __mod__(self, other):
        return Imaginary(
            (
                    str(self.imaginary_part % other.imaginary_part)
                    + "i+"
                    + str(self.real_part % other.real_part)
            )
        )

    def format(self, latex=False):
        """
        formats an imaginary number into mathematical format.
        :return: str
        """
        real = str(self.real_part)
        imaginary = str(self.imaginary_part)

        if real == "0":
            real = ""

        if imaginary == "0":
            imaginary = ""

        if not latex:
            ans = str(real) + "+" + str(imaginary) + "i"
        elif latex:
            ans = "$" + str(real) + "+" + str(imaginary) + "i" + "$"
        else:
            raise ValueError("Parameter latex should be a boolean")
        return ans
