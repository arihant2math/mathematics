from mathematics import number_theory, lists


def grow_prime(far):
    primes = lists.primes
    for i in range(len(primes), far):
        if number_theory.is_prime(i):
            primes.append(i)
    lists.primes = primes
