"""__init__ of mathematics package"""
from mathematics.function import solve

VERSION = '0.0.0-alpha0'
__version__ = VERSION


def product(list_of_numbers):
	"""
	Returns the product of a list of numbers.
	"""
	current_product = 1
	for number in list_of_numbers:
		current_product *= number
	return current_product


def sigma(func, start, stop):
	"""The sigma function returns the sum of the values of the function func from start to stop."""
	return sum(func(i) for i in range(start, stop + 1))


def pi(func, start, stop):
	"""The pi function returns the product of the values of the function func from start to stop."""
	ans = 1
	for i in range(start, stop + 1):
		ans *= func(i)
	return ans
