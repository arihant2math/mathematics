import math
from datetime import datetime
from multiprocessing import Pool


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


def prime_gen(start, stop=None, multiprocess=True):
    """Generates primes from start=>stop"""
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


if __name__ == "__main__":
    t1 = datetime.now()
    print(prime_gen(0, 10000), False)
    t2 = datetime.now()
    t3 = datetime.now()
    print(prime_gen(0, 10000), True)
    t4 = datetime.now()
    print((t2-t1).microseconds)
    print((t4-t3).microseconds)


def mersenne(n):
    """
    Returns the mersenne of the number ((2**n)-1)
    :param n:
    :return:
    """
    return (2 ** n) - 1


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
            print(lucas_lehmer((i ** 2) - 1))
            answer.append((i ** 2) - 1)
    return answer


def prime_factor(number):
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
