import math
import itertools


def factors(number):
    """Returns the factors of the number"""
    return [i for i in range(1, number + 1) if not number % i]


def step_in_euclidean_algorithm(a, b):
    x, y = divmod(a, b)
    return a, b, x, y


def euclidean_algorithm(a, b, pretty_print=False):
    li = step_in_euclidean_algorithm(a, b)
    while li[3] != 0:
        li = step_in_euclidean_algorithm(li[1], li[3])
    if pretty_print:
        return (
            str(li[0]) + " = " + str(li[1]) + "(" + str(li[2]) + ")" + "+" + str(li[3])
        )
    else:
        return li


def extended_euclidean_algorithm():
    # should have param number
    return NotImplemented


def nth_power(stop, power):
    return [i**power for i in range(1, stop + 1)]


def d(n, m):
    """Checks if n divides m, equivalent to n|m"""
    if (m / n) % 1 == 0:
        return True
    return False


def partition(n):
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
                if new_part.sort() not in partitions:
                    partitions.append(new_part.sort())
    return partitions.sort()


def primitive_root(n):
    primitive_roots = []
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
    if len(primitive_roots) == 0:
        for w, y in itertools.product(range(2, n), repeat=2):
            number = []
            for x in range(1, n):
                for z in range(1, n):
                    if (math.gcd(w, n) == 1) and (math.gcd(y, n) == 1):
                        if not (pow(w, x) * pow(y, z)) % n in number:
                            number.append((pow(w, x) * pow(y, z)) % n)
            if len(number) == n / 2 - ((n / 2) % 1):
                return str(w) + ", " + str(y)
    return None


def root_equivalents(modulus, square_of_root):
    return [i for i in range(0, modulus) if i ** 2 % modulus == square_of_root]


def pigeon_hole(colors, number_needed):
    return (number_needed - 1) * colors


def primitive_roots(n):
    primitive_roots = []
    co_prime_to_n = []
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            co_prime_to_n.append(i)
    for i in range(1, n):
        powers_of_i = []
        for e in range(1, n):
            powers_of_i.append(i**e % n)
        if sorted(powers_of_i) == co_prime_to_n:
            primitive_roots.append(i)
    return primitive_roots
