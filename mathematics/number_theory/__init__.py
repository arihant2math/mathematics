import math
import itertools

from mathematics.number_theory.primes import is_prime


def totient(m: int) -> int:
    """The euler totient function returns the number of positive integers less than or equal to m that are relatively
    prime to m.
    :return: The number of positive integers less than or equal to m that are relatively prime to m.
    """
    units = [i for i in range(1, m + 1) if math.gcd(i, m) == 1]
    return len(units)


def factors(number: int) -> list[int]:
    """Returns the factors of the number"""
    return [i for i in range(1, number + 1) if not number % i]


def step_in_euclidean_algorithm(a, b) -> tuple:
    x, y = divmod(a, b)
    return a, b, x, y


def euclidean_algorithm(a, b):
    li = step_in_euclidean_algorithm(a, b)
    while li[3] != 0:
        li = step_in_euclidean_algorithm(li[1], li[3])
    return li


def extended_euclidean_algorithm():
    # should have param number
    raise NotImplementedError("To be implemented release TBD")


def nth_power(repetitions, power) -> list[int]:
    """returns a list with every i from 1 to repetitions with every element raised to the power"""
    return [i ** power for i in range(1, repetitions + 1)]


def d(n: int, m: int) -> bool:
    """Checks if n divides m, equivalent to n|m"""
    return (m / n) % 1 == 0


def partition(n: int) -> list[list[int]]:
    """Returns the partitions of n"""
    partitions = []
    ll = ""
    for i in range(1, n + 1):
        ll += str(i)
    for i in range(1, n + 1):
        combination = itertools.product(ll, repeat=i)
        for element in combination:
            z = 0
            for character in element:
                z += int(character)
            if z == n:
                new_part = []
                for item in element:
                    new_part.append(int(item))
                new_part.sort()
                if new_part not in partitions:
                    partitions.append(new_part)
    partitions.sort()
    return partitions


def primitive_root(n: int):
    _primitive_roots = []
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            number = []
            power = pow(i, 2) % n
            while (power != i) and (power != 0) and (power != 1):
                if power not in number:
                    number.append(power)
                power = pow(2, 2) % n
                if len(number) == n:
                    return i, number
    if len(_primitive_roots) == 0:
        for w, y in itertools.product(range(2, n), repeat=2):
            number = []
            for x in range(1, n):
                for z in range(1, n):
                    if (math.gcd(w, n) == 1) and (math.gcd(y, n) == 1):
                        if not (pow(w, x) * pow(y, z)) % n in number:
                            number.append((pow(w, x) * pow(y, z)) % n)
            if len(number) == n / 2 - ((n / 2) % 1):
                return w, y
    return None


def root_equivalents(modulus: int, square_of_root: int) -> list[int]:
    return [i for i in range(0, modulus) if i ** 2 % modulus == square_of_root]


def pigeon_hole(colors: int, number_needed: int) -> int:
    return (number_needed - 1) * colors


def primitive_roots(n: int) -> list:
    primitive_roots_l = []
    co_prime_to_n = []
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            co_prime_to_n.append(i)
    for i in range(1, n):
        powers_of_i = []
        for e in range(1, n):
            powers_of_i.append(i**e % n)
        if sorted(powers_of_i) == co_prime_to_n:
            primitive_roots_l.append(i)
    return primitive_roots_l


def prime_factor(number: int) -> list[int]:
    """Returns a list of prime factors of a number"""
    if number == 1:
        return [1]
    ans = []
    for i in range(2, number + 1):
        if is_prime(i):
            while number % i == 0:
                if number % i == 0:
                    ans.append(i)
                    number = int(number / i)
    return ans
