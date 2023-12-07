import itertools
import statistics

import mathematics.number_theory.primes
from mathematics import number_theory
import math


def partial_sum_for_half_plus_fourth(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    return result


# function that returns all primes up to that number.
def sieve_numbers(num):
    square_root_sieve = []
    sieve = range(2, num + 1)
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if i in sieve:
            square_root_sieve.append(i)
            new_sieve = []
            for x in sieve:
                if x != i and x % i != 0:
                    new_sieve.append(x)
            sieve = new_sieve
    return square_root_sieve + sieve


# Patterns for modular arithmetic
def pattern_mod_n_adding(n, mod):
    ans = []
    number = n % mod
    new_number = 2 * number
    print(number)
    while number != new_number:
        ans.append(new_number % mod)
        new_number = (number + new_number) % mod
    return ans


def pattern_mod_n_multiplying(number, mod):
    x = number % mod
    result = []
    actual = x * x
    while x != actual:
        result.append(actual)
        actual = actual * x
    return result


def pattern_mod_n_multiplying_gen(end, start_1, start_2):
    lengths = []
    for i in range(start_1, end):
        for dictionary in range(start_2, i):
            pattern_mod_n_multiplying(dictionary, i)
            z = int(len(pattern_mod_n_adding(dictionary, i)))
            lengths.append(z)
    return lengths


def pattern_mod_n_adding_gen(end, start_1, start_2):
    lengths = []
    for mod in range(start_1, end):
        print("mod=" + str(mod) + ":")
        for number in range(start_2, mod):
            print("mod=" + str(mod) + " number=" + str(number) + ":")
            print()
            print(pattern_mod_n_adding(number, mod))
            z = int(len(pattern_mod_n_adding(number, mod)))
            print("The length is " + str(z))
            lengths.append(z)
    return lengths


def pattern_mod_n_analytics_v1(
    end_1, start_1_1, start_2_1, end_2, start_1_2, start_2_2, the_function
):
    global first, last
    if "add" in the_function:
        first = pattern_mod_n_adding_gen(end_1, start_1_1, start_2_1)
        last = pattern_mod_n_adding_gen(end_2, start_1_2, start_2_2)
    elif "multiplication" in the_function:
        first = pattern_mod_n_multiplying_gen(end_1, start_1_1, start_2_1)
        last = pattern_mod_n_multiplying_gen(end_2, start_1_2, start_2_2)
    for key in first:
        print(str(key) + str(float(last[key]) - float(first[key])))


def addition_sums_mod_n(n):
    x = 0
    for i in range(1, n):
        x += i
    return x % n


def addition_sums_mod_n_gen(start, stop):
    for i in range(start, stop):
        print(addition_sums_mod_n(i))
        pass


def pattern_mod_n_adding_gen_primes(end, start_1, start_2):
    lengths = []
    for mod in range(start_1, end + 1):
        if mathematics.number_theory.primes.is_prime(mod):
            print("mod=" + str(mod) + ":")
            for number in range(start_2, mod):
                print(
                    "mod="
                    + str(mod)
                    + " number="
                    + str(number)
                    + ":"
                    + str(pattern_mod_n_adding(number, mod))
                )
                z = int(len(pattern_mod_n_adding(number, mod)))
                print("The length is " + str(z))
                lengths.append(z)
    print(lengths)
    print("The mean is:" + str(statistics.mean(lengths)))
    print("The median is:" + str(statistics.median(lengths)))
    print("The max is:" + str(max(lengths)))
    print("The min is:" + str(min(lengths)))
    print(
        "Interquartile range:"
        + str(statistics.median_high(lengths) - statistics.median_low(lengths))
    )
    dictionary = {
        "Interquartile_range": str(
            statistics.median_high(lengths) - statistics.median_low(lengths)
        ),
        "1st quartile": str(statistics.median_low(lengths)),
        "Third_quartiles": str(statistics.median_high(lengths)),
        "mean": float(statistics.mean(lengths)),
        "median": statistics.median(lengths),
    }
    return dictionary


def prime_mult(n):
    result = 1
    for i in range(2, n):
        result *= i
    result = result % n
    print(result)


def prime_mult_gen(n):
    for i in range(1, n):
        if mathematics.number_theory.primes.is_prime(i):
            prime_mult(i)


def powers_of_x_plus_1_mod_prime(prime, x, p):
    ans = (pow((x + 1), p)) % prime
    return ans


def powers_of_x_plus_1_mod_prime_gen(x, prime, stop_p):
    for p in range(1, stop_p + 1):
        return powers_of_x_plus_1_mod_prime(prime, x, p)

def squares_mod_m(stop, m):
    beginning = number_theory.nth_power(stop, 2)
    ans = []
    for item in beginning:
        number = int(item) % m
        ans.append(number)
    return ans


def nth_power_mod_m(stop, m, power):
    beginning = number_theory.nth_power(stop, power)
    ans = []
    check = 1
    for item in beginning:
        number = int(item) % m
        if check == number and item != 1:
            return ans
        ans.append(number)
    return ans


def distance(mod, number):
    if number != mod:
        ans = [number]
        count = 2
        cont = True
        while cont:
            if (number**count) % mod != number:
                ans.append((number**count) % mod)
            else:
                cont = False
                return ans
            count += 1
    else:
        pass


def special_exclusion_partition(n, i):
    x = number_theory.partition(n)
    for item in x:
        if str(i) not in item:
            x.remove(item)
    return x


def root_equivalents(modulus, root):
    root_equivalent = []
    for i in range(0, modulus):
        if i**2 % modulus == root:
            root_equivalent.append(i)
    print(root_equivalent)


def sum_set(set_a, set_b):
    """Adds the sets, not the same as union"""
    sum_a_b = []
    for a in set_a:
        for b in set_b:
            sum_a_b.append(a + b)
    sum_a_b = set(sum_a_b)
    return sum_a_b
