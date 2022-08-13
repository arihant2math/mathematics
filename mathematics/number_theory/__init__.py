import math
import itertools


# Prime stuff


def is_prime_wilsons_theorem(num):
    """Check for primality using wilsons theorem"""
    if num == 1 or num == 0:
        return False
    if num < 0:
        return False
    num = num
    return math.factorial(num - 1) % num == num - 1


def is_prime_fermat_little_theorem(num):
    """Check for primality using fermats little theorem, faster than wilsons theorem for larger numbers"""
    if num == 1 or num == 0:
        return False
    return all(i ** (num - 1) % num == 1 for i in range(2, num))


def is_prime(num):
    """Checks if the number is prime using fermats little theorem if the number is greater that 1000"""
    if num == 1 or num == 0:
        return False
    if num < 0:
        return False
    if num > 1000:
        return all(i ** (num - 1) % num == 1 for i in range(2, num))
    n = abs(num)
    return math.factorial(n - 1) % n == n - 1


def prime_gen(start, stop=None):
    """Generates primes from start=>stop"""
    if stop is None:
        stop = start
        start = 0
    ans = []
    for i in range(start, stop):
        if is_prime(i):
            ans.append(i)
    return ans


def mersenne(n):
    """
    Returns the mersenne of the number ((2**n)-1)
    :param n:
    :return:
    """
    return (2**n) - 1


def lucas_lehmer(m):
    """Implements Lucas Lehmer mersenne prime test."""
    lucas_lehmer_list = [4]
    if len(lucas_lehmer_list) < m:
        for num in range(m - 1):
            lucas_lehmer_list.append(lucas_lehmer_list[-1] ** 2 - 2)
            print(lucas_lehmer_list)
    if lucas_lehmer_list[m - 1] == 0:
        return True
    else:
        return False


def lucas_lehmer_gen(start, stop):
    answer = []
    for i in range(start, stop + 1):
        if lucas_lehmer(i):
            print(lucas_lehmer((i**2) - 1))
            answer.append((i**2) - 1)
    return answer


def prime_factor(number):
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


def factors(number):
    return [i for i in range(1, number + 1) if not number % i]


def step_in_euclidean_algorithm(a, b):
    x, y = divmod(a, b)
    return a, b, x, y


def euclidean_algorithm(a, b, want_fancy=False):
    li = step_in_euclidean_algorithm(a, b)
    while li[3] != 0:
        li = step_in_euclidean_algorithm(li[1], li[3])
    if want_fancy:
        return (
            str(li[0]) + " = " + str(li[1]) + "(" + str(li[2]) + ")" + "+" + str(li[3])
        )
    else:
        return li


# def extended_euclidean_algorithm():
#     # should have param number
#     return NotImplemented


def lcm(m, n):
    result = m * n / math.gcd(m, n)
    return result


def totient_function(m, return_units=False):
    units = [i for i in range(1, m + 1) if math.gcd(i, m) == 1]
    ans = len(units)
    if return_units:
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
