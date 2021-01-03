import math


class Number(int):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def __or__(self, sec_num):
        if (sec_num / self.num) % 1 == 0:
            return True
        else:
            return False


class Prime(Number):
    def __init__(self, num):
        super().__init__(num)
        if math.factorial(num - 1) % num != -1:
            raise Exception("Number is not prime. ")
        self.num = num


class Merrsene(Prime):
    def __init__(self, num):
        super().__init__(num)


class SofieGermain(Prime):
    def __init__(self, num):
        super().__init__(num)


class Fraction:
    def __init__(self, numerator, denominator):
        self.num = int(numerator)
        if denominator == 0:
            raise ZeroDivisionError
        if denominator > 0:
            self.denom = int(denominator)
        else:
            self.denom = abs(denominator)
            self.num = -self.num

    def __str__(self):
        div_by = math.gcd(self.num, self.denom)
        return str(self.num // div_by) + "/" + str(self.denom // div_by)

    def __add__(self, other):
        # return Fraction((self.numerator + other.numerator), (self.denominator + other.denominator))
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __bool__(self):
        return True

    def __pow__(self, power, modulo=None):
        pass

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)


class Imaginary:
    def __init__(self, num):
        num = str(num).lower()
        breaker = []
        for item in num:
            if item != " ":
                breaker.append(item)
        num = ""
        for item in breaker:
            num = num + item

        self.math_form = num
        imaginary_part = ""
        real_part = ""
        right_side_now = False
        which_is_imaginary = True
        for item in num:
            if item == "+":
                right_side_now = True
            else:
                if right_side_now:
                    if item != "i":
                        imaginary_part = imaginary_part + item
                else:
                    if item != "i":
                        real_part = real_part + item
                    if item == "i":
                        which_is_imaginary = False
        if which_is_imaginary:
            if imaginary_part != "":
                self.imaginary_part = int(imaginary_part)
            else:
                self.imaginary_part = 1
            self.real_part = int(real_part)
        else:
            if real_part != "":
                self.imaginary_part = int(real_part)
            else:
                self.imaginary_part = 1
            self.real_part = int(imaginary_part)

    def __str__(self):
        return self.math_form

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.imaginary_part + other.imaginary_part
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __sub__(self, other):
        real = self.real_part - other.real_part
        imaginary = self.imaginary_part - other.imaginary_part
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __mul__(self, other):
        real = (self.real_part * other.real_part) - (self.imaginary_part * other.real_part)
        imaginary = (self.imaginary_part * other.real_part) + (self.real_part * other.imaginary_part)
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __truediv__(self, other):
        real = (self.real_part / other.real_part) - (self.imaginary_part / other.real_part)
        imaginary = (self.imaginary_part / other.real_part) + (self.real_part / other.imaginary_part)
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __floordiv__(self, other):
        real = (self.real_part // other.real_part) - (self.imaginary_part // other.real_part)
        imaginary = (self.imaginary_part // other.real_part) + (self.real_part // other.imaginary_part)
        ans = str(real) + "+" + str(imaginary) + "i"
        return Imaginary(ans)

    def __pow__(self, power, modulo=None):
        if not (modulo is None):
            return NotImplemented
        ans = self
        for i in range(0, power):
            ans = ans * self
        return Imaginary(ans)

    def __mod__(self, other):
        return NotImplemented

    def format(self):
        real = self.real_part
        imaginary = self.imaginary_part
        # not finished
        ans = str(real) + "+" + str(imaginary) + "i"
        return ans


class Variable:
    def __init__(self, s=None, name=None, coefficient=None, power=None):
        if (s is not None) and ((name is None) or (coefficient is None)):
            odd = [" ", "@", "*", "&"]
            breaker = []
            for item in s:
                if item != " ":
                    breaker.append(item)
            s = ""
            after_name = False
            right_after_name = False
            second = 1
            for item in breaker:
                if right_after_name:
                    if item == "*":
                        right_after_name = False
                        odd = True
                elif (name is None) and (str(item).isalpha()) and (item not in odd):
                    name = item
                    breaker.remove(item)
                    right_after_name = True
                elif (name is not None) and (str(item).isalpha()) and (item not in odd):
                    print("error You have to have one variable name")

            if (breaker[len(breaker) - 1] == "*") and (len(breaker) >= 1):
                breaker.remove(breaker[len(breaker) - 1])
            coefficient = ""
            for item in breaker:
                coefficient = coefficient + item
        self.name = str(name)
        if coefficient is None:
            self.coefficient = 1
        self.coefficient = int(coefficient)
        if power is None:
            power = 1
        self.power = power

    def __str__(self):
        if self.coefficient != 1:
            return str(self.coefficient) + str(self.name)
        elif self.coefficient == 1:
            return str(self.name)

    def __add__(self, other):
        if other.name == self.name:
            return Variable(name=self.name, coefficient=self.coefficient + other.coefficient)
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name

    def __sub__(self, other):
        if other.name == self.name:
            return Variable(name=self.name, coefficient=self.coefficient + other.coefficient)
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name

    def __mul__(self, other):
        if other.name == self.name:
            return Variable(name=self.name, coefficient=(self.coefficient * other.coefficient),
                            power=(self.power + other.power))
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name

    def __truediv__(self, other):
        if other.name == self.name:
            return Variable(name=self.name, coefficient=(self.coefficient / other.coefficient),
                            power=(self.power - other.power))
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name

    def __floordiv__(self, other):
        if other.name == self.name:
            return Variable(name=self.name, coefficient=(self.coefficient // other.coefficient),
                            power=(self.power - other.power))
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name

    def __pow__(self, power, modulo=None):
        pass

    def __abs__(self):
        return Variable(name=self.name, coefficient=abs(self.coefficient))


class Expression:
    def __init__(self, expression):
        breaker = []
        terms = []
        term = ""
        for item in expression:
            if item != ' ':
                breaker.append(item)
        for item in breaker:
            if item == "+":
                terms.append(term)
                term = ""
            else:
                term += item
        breaker = []
        for term in terms:
            for item in term:
                if item.isalpha():
                    breaker.append(Variable(term))
                    break
        self.terms = breaker
        self.expression = expression

    def __str__(self):
        return self.terms

    def simplify(self):
        for item in self.terms:
            pass


class Equation:
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2


print(Fraction(3, 7))
print(Fraction(4, 10))
print(Fraction(0, 10))
print(Fraction(-4, 10))
print(Fraction(4, -10))
print(Fraction(4, 0))
