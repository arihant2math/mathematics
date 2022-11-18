import mathematics.number_theory.primes as p
from mathematics import lists


def grow_prime(stop):
    primes = lists.primes.read()
    if len(primes) == 0:
        primes = [2]
    if primes[-1] > stop:
        return
    for i in range(primes[-1] + 1, stop):
        if p.is_prime(i):
            primes.append(i)
    lists.primes.modify(primes)
    lists.primes.save()
