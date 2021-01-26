"""This implements algebraic classes"""
import math


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
        elif type(power) == Fraction:
            return (self.num ** power.num) ** (1.0/float(power.denominator))
        else:
            raise TypeError

    def sum_digits(self):
        """Returns the sum of all the digits"""
        str_num = str(self.num)
        ans = Number(0)
        for item in str_num:
            ans += Number(item)
        return ans

    def product_digits(self):
        """Returns the sum of all the digits"""
        str_num = str(self.num)
        ans = Number(0)
        for item in str_num:
            ans *= int(item)
        return ans


class Fraction:
    """A fraction class that emulates a fraction"""

    def __init__(self, s="", numerator=None, denominator=None):
        if (numerator is None) or (denominator is None):
            s = str(s)
            numerator = ""
            denominator = ""
            is_numerator = True
            for item in s:
                if item != " ":
                    if item == "/":
                        is_numerator = False
                    elif is_numerator:
                        numerator += item
                    else:
                        denominator += item
        self.num = int(numerator)
        if denominator == 0:
            raise ZeroDivisionError
        if int(denominator) > 0:
            self.denominator = Number(denominator)
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


class Imaginary:
    """
    emulates an imaginary number.
    """

    def __init__(self, num):
        num = str(num).lower()
        breaker = []
        for item in num:
            if item != " ":
                breaker.append(item)
        num = ""
        for item in breaker:
            num += item

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
                        imaginary_part += item
                else:
                    if item != "i":
                        real_part += item
                    if item == "i":
                        which_is_imaginary = False
        if which_is_imaginary:
            if imaginary_part != "":
                self.imaginary_part = Number(imaginary_part)
            else:
                self.imaginary_part = 1
            self.real_part = Number(real_part)
        else:
            if real_part != "":
                self.imaginary_part = Number(real_part)
            else:
                self.imaginary_part = 1
            self.real_part = Number(imaginary_part)

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
        ans = self
        for i in range(0, power):
            ans = ans * self
        return Imaginary(ans)

    def __mod__(self, other):
        return Imaginary((str(self.imaginary_part % other.imaginary_part)+"i+"+str(self.real_part % other.real_part)))

    def format(self, latex=False):
        """
        formats an imagery number into mathematical format.
        :return: str
        """
        real = self.real_part
        imaginary = self.imaginary_part
        if not latex:
            ans = str(real) + "+" + str(imaginary) + "i"
        else:
            ans = "$" + str(real) + "+" + str(imaginary) + "i" + "$"
        return ans


class Variable:
    """
    Emulates a Variable
    """

    def __init__(self, s="", name=None, coefficient=None, power=None):
        """
        :type s: str
        :type name: str
        :type coefficient: int
        :type power: int
        """
        if (name is None) or (coefficient is None):
            odd = [" ", "@", "*", "&"]
            breaker = []
            for item in s:
                if item != " ":
                    breaker.append(item)
            right_after_name = False
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
                coefficient += item
        self.name = str(name)
        if coefficient is None:
            self.coefficient = 1
        self.coefficient = Number(coefficient)
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

    def __neg__(self):
        return Variable(coefficient=self.coefficient.__neg__(), power=self.power, name=self.name)

    def __pow__(self, power, modulo=None):
        return Variable(name=self.name, coefficient=(self.coefficient ** power), power=(self.power*power))

    def __abs__(self):
        return Variable(name=self.name, coefficient=abs(self.coefficient))


class Term:
    def __init__(self, s):
        breaker = []
        has_variable = False
        for item in s:
            if not has_variable:
                if item == "*" or "/":
                    raise Exception("Not a term")
                elif item.isalpha:
                    has_variable = True
                elif item != " ":
                    breaker.append(item)
        if has_variable:
            self.operate = Variable(s=s)
        else:
            self.operate = Number(s)
        self.has_variable = has_variable

    def __neg__(self):
        self.operate.__neg__()

    def simplify(self):
        if self.has_variable:
            self.operate.simplify


class Expression:
    def __init__(self, expression):
        breaker = []
        terms = []
        term = ""
        for item in expression:
            if item != ' ':
                breaker.append(item)
        positive = True
        for item in breaker:
            if item == "+":
                positive = True
                if positive:
                    terms.append(Term(term))
                    term = ""
                else:
                    terms.append(-Term(term))
                    term = ""
            elif item == "-":
                positive = False
                if positive:
                    terms.append(Term(term))
                    term = ""
                else:
                    terms.append(-Term(term))
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
            item.simplify()


class Equation:
    def __init__(self, expression_one, expression_two):
        self.expression_one = Expression(expression_one)
        self.expression_two = Expression(expression_two)
        self.expression_one.simplify()
        self.expression_two.simplify()
