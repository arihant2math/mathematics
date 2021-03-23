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
        ans = Number(0)
        for item in str_num:
            ans *= int(item)
        return ans


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
        self.__simplify()

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


class Imaginary:
    """
    emulates an imaginary number.
    """

    def __init__(self, num):
        num = str(num).lower().replace(" ", "").split("+")
        if "i" in num[0]:
            self.imaginary_part = int(num[0][1:len(num[0])])
            self.real_part = Number(num[2])
        else:
            self.imaginary_part = int(num[0][1:len(num[0])])
            self.real_part = Number(num[2])

    def __str__(self):
        return str(self.real_part) + " + " + str(self.imaginary_part) + "i"

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
        return Imaginary(
            (str(self.imaginary_part % other.imaginary_part) + "i+" + str(self.real_part % other.real_part)))

    def format(self, latex=False):
        """
        formats an imaginary number into mathematical format.
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
        if (name is None) or (coefficient is None) or (power is None):
            s.replace("*", " ")
            s.replace("^", "pow")
            sl_old = s.split("*")
            sl = []
            for item in sl_old:
                sl.append(item.split("pow"))
            if str(sl[0]).isalpha():
                self.name = str(sl[0][0])
                self.power = int(sl[0][1])
                if len(sl) == 2:
                    self.coefficient = int(sl[1][0])
                else:
                    self.coefficient = 1
            else:
                self.name = str(sl[1][0])
                if len(sl[1]) == 2:
                    self.power = int(sl[1][1])
                else:
                    self.power = 1
                self.coefficient = int(sl[0][0])
        else:
            self.power = power
            self.coefficient = coefficient
            self.name = name

    def __str__(self):
        if self.coefficient != 1:
            return str(self.coefficient) + str(self.name)
        elif self.coefficient == 1:
            return str(self.name)

    def __add__(self, other):
        if (other.name == self.name) and (other.power == self.power):
            return Variable(name=self.name, coefficient=self.coefficient + other.coefficient, power=self.power)
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name
        else:
            return "error the powers are not equal"

    def __sub__(self, other):
        if (other.name == self.name) and (other.power == self.power):
            return Variable(name=self.name, coefficient=self.coefficient - other.coefficient)
        elif other.name != self.name:
            return "error " + other.name + " != " + self.name
        else:
            return "error the powers are not equal"

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
        return Variable(name=self.name, coefficient=(self.coefficient ** power), power=(self.power * power))

    def __abs__(self):
        return Variable(name=self.name, coefficient=abs(self.coefficient))


class Term:
    """
    A term
    """

    def __init__(self, s):
        term = []
        current_var = ""
        for item in s:
            if not s.isalpha:
                current_var += item
            else:
                term.append(Variable(current_var))
                current_var = item
        self.term = term

    def __neg__(self):
        to_return = ""
        for item in self.term:
            to_return += (-item)
        return Variable(to_return)

    def simplify(self):
        """
        Will simplify the term
        """
        pass


class Expression:
    """
    Expression class
    """

    def __init__(self, expression):
        expression = expression.replace("-", "+-")
        breaker = expression.split("+")
        self.terms = []
        for item in breaker:
            self.terms.append(Term(item))

    def __str__(self):
        return self.terms

    def simplify(self):
        """
        Simplifies the expression, does not return anything
        """
        for item in self.terms:
            item.simplify()


class Equation:
    """Equation"""

    def __init__(self, s, expression_one, expression_two):
        if (expression_one is None) or (expression_two is None):
            s = s.replace(" ", "").split("=")
            self.expression_one = s[0]
            self.expression_two = s[1]
        else:
            self.expression_one = Expression(expression_one)
            self.expression_two = Expression(expression_two)
        self.expression_one.simplify()
        self.expression_two.simplify()

    def degree(self):
        """
        Finds the degree
        """
        max_power = 0
        for term in self.expression_one.terms:
            for var in term.term:
                if var.power > max_power:
                    max_power = var.power

        for term in self.expression_two.terms:
            for var in term.term:
                if var.power > max_power:
                    max_power = var.power
        return max_power

    def number_of_vars(self):
        """
        Finds the number of different variables in the equation.
        """
        var_list = []
        for term in self.expression_one.terms:
            for var in term.term:
                if var.name not in var_list:
                    var_list.append(var.name)
        for term in self.expression_two.terms:
            for var in term.term:
                if var.name not in var_list:
                    var_list.append(var.name)

    def solve(self):
        """
        solves the equation
        """
        d = self.degree()
        if d == 1:
            if self.number_of_vars() != 1:
                raise Exception(NotImplementedError)
            else:
                expression_one_list = []
                expression_two_list = []
                for term in self.expression_one.terms:
                    for var in term.term:
                        expression_one_list.append(var)
                for term in self.expression_two.terms:
                    for var in term.term:
                        expression_two_list.append(var)

                for item in expression_one_list:
                    for thing in expression_two_list:
                        if item.name == thing.name:
                            pass
