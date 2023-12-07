import mathematics.number_theory.primes as p
from mathematics import lists


def grow_prime(stop):
    primes = p.prime_gen(stop, multiprocess=False)
    lists.primes.write(primes)
