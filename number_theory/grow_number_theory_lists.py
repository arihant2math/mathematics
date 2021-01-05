from number_theory import numbertheorylists
import number_theory_essensials
far = input("How much do you want to grow the primes list")
numbertheorylists.primes = []
numbertheorylists.primes = number_theory_essensials.prime_gen(1, int(far) + 1)
