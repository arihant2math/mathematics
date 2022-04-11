from mathematics import number_theory
import math
import itertools


def test_is_prime_wilsons_theorem():
    assert not number_theory.is_prime_wilsons_theorem(1)
    assert number_theory.is_prime_wilsons_theorem(2)
    assert number_theory.is_prime_wilsons_theorem(3)
    assert not number_theory.is_prime_wilsons_theorem(4)
    assert number_theory.is_prime_wilsons_theorem(5)
    assert not number_theory.is_prime_wilsons_theorem(10)
    assert number_theory.is_prime_wilsons_theorem(11)
    assert not number_theory.is_prime_wilsons_theorem(93)


def test_is_prime_fermat_little_theorem():
    assert not number_theory.is_prime_fermat_little_theorem(1)
    assert number_theory.is_prime_fermat_little_theorem(2)
    assert number_theory.is_prime_fermat_little_theorem(3)
    assert not number_theory.is_prime_fermat_little_theorem(4)
    assert number_theory.is_prime_fermat_little_theorem(5)
    assert not number_theory.is_prime_fermat_little_theorem(10)
    assert number_theory.is_prime_fermat_little_theorem(11)
    assert not number_theory.is_prime_fermat_little_theorem(93)


def test_is_prime():
    assert not number_theory.is_prime(1)
    assert number_theory.is_prime(2)
    assert number_theory.is_prime(3)
    assert not number_theory.is_prime(4)
    assert number_theory.is_prime(5)
    assert not number_theory.is_prime(10)
    assert number_theory.is_prime(11)
    assert not number_theory.is_prime(93)


def test_prime_gen():
    assert number_theory.prime_gen(100) == number_theory.prime_gen(0, 100)


def test_mersenne():
    assert number_theory.mersenne(3) == 7
    assert number_theory.mersenne(5) == 31


# def test_lucas_lehmer():
#     assert lucas_lehmer(7)
#     assert lucas_lehmer(31)


def lucas_lehmer_gen(start, stop):
    answer = []
    for i in range(start, stop + 1):
        if number_theory.lucas_lehmer(i):
            print(number_theory.lucas_lehmer((i**2) - 1))
            answer.append((i**2) - 1)
    return answer


def test_prime_factor():
    assert number_theory.prime_factor(1) == [1]
    assert number_theory.prime_factor(11) == [11]
    assert number_theory.prime_factor(100) == [2, 2, 5, 5]


def test_factor():
    assert number_theory.factors(1) == [1]
    assert number_theory.factors(10) == [1, 2, 5, 10]
    assert number_theory.factors(20) == [1, 2, 4, 5, 10, 20]
    assert number_theory.factors(22) == [1, 2, 11, 22]
    assert number_theory.factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]


def test_lcm():
    assert number_theory.lcm(10, 5) == 10
    assert number_theory.lcm(14, 20) == 140


def totient_function(m, print_units):
    units = [i for i in range(1, m + 1) if math.gcd(i, m) == 1]
    ans = len(units)
    if print_units:
        return ans, units
    else:
        return ans


def nth_power(stop, power):
    return [i**power for i in range(1, stop + 1)]


def pascal_triangle(n, k):
    return int(((math.factorial(n)) / (math.factorial(n - k) * math.factorial(k))))


def pascals_triangle(stop):
    ans = []
    for n in range(1, stop + 1):
        length = []
        for k in range(0, n + 1):
            length.append(pascal_triangle(n, k))
        ans.append(length)
    return ans


def d(n, m):
    if (m / n) % 1 == 0:
        return True


def partition(n):
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
                if sorted(new_part) not in partitions:
                    partitions.append(new_part)
    return partitions


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
