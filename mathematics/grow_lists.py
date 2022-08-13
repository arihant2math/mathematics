from mathematics import number_theory, lists


def grow_prime(stop):
    primes = lists.primes.read()
    if len(primes) == 0:
        primes = [2]
    if primes[-1] > stop:
        return
    for i in range(primes[-1] + 1, stop):
        if number_theory.is_prime(i):
            primes.append(i)
    lists.primes.modify(primes)
    lists.primes.save()
