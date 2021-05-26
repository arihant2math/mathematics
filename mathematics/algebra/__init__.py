"""This implements algebraic classes"""
import math
from mathematics.algebra.Number import Number
from mathematics.algebra.Fraction import Fraction


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
            print(s)
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

    def __init__(self, s, expression_one=None, expression_two=None):
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
