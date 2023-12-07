import math
from multiprocessing import Pool


def is_prime_wilsons_theorem(num):
    """Check for primality using wilsons theorem"""
    if num == 1 or num == 0 or num < 0:
        return False
    num = num
    return math.factorial(num - 1) % num == num - 1


def is_prime_fermat_little_theorem(num):
    """Check for primality using fermats little theorem, faster than wilsons theorem for larger numbers,
    but is incorrect for any Carmicheal number"""
    if num == 1 or num == 0:
        return False
    return all(i ** (num - 1) % num == 1 for i in range(2, num))


def is_prime_six_k_pm_one(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_prime(num: int) -> bool:
    """Uses 6k+-1"""
    return is_prime_six_k_pm_one(num)


def prime_gen(*args, **kwargs):
    """Generates primes from start=>stop"""
    start = 0
    stop = 0
    if len(args) == 1:
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]
    multiprocess = False
    if "multiprocess" in kwargs.items():
        multiprocess = kwargs["multiprocess"]
    primes_to_check = list(range(start, stop))
    result = []
    if multiprocess:
        with Pool() as p:
            result = p.map(is_prime, primes_to_check)
    else:
        for i in primes_to_check:
            if is_prime(i):
                result.append(i)
    actual_numbers = []
    for count, prime in enumerate(result):
        if prime:
            actual_numbers.append(count + start)
    return actual_numbers


def mersenne(n):
    """
    Returns the nth mersenne number
    :param n:
    :return:
    """
    return (2**n) - 1


def is_mersenne_number(n):
    return math.log(n + 1, 2).is_integer()


def lucas_lehmer(p):
    """Implements Lucas Lehmer mersenne prime test. Checks if the pth mersenne number is prime"""
    s = 4
    m = mersenne(p)
    for i in range(p - 2):
        s = ((s * s) - 2) % m
    return s == 0


def lucas_lehmer_gen(start, stop):
    answer = []
    for i in range(start, stop):
        if lucas_lehmer(i):
            print(lucas_lehmer((i**2) - 1))
            answer.append((i**2) - 1)
    return answer
