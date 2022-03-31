import itertools
import math


def totient(m, print_units=False):
    units = []
    for i in range(1, m):
        if math.gcd(i, m) == 1:
            units.append(i)
    ans = len(units)
    if not print_units:
        return ans
    else:
        return ans, units


def partition(n):
    partitions = []
    le = ""
    for i in range(1, n + 1):
        le += str(i)
    for i in range(1, n + 1):
        for element in itertools.product(le, repeat=i):
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


def combination(n, k):
    num = math.factorial(n)
    den = math.factorial(n - k) * math.factorial(k)
    return num / den


def permutation(n, k):
    num = math.factorial(n)
    den = math.factorial(n - k)
    return num / den


def generate_combinations(string, r):
    if r == 1:
        n = []
        for element in string:
            n.append(element)
    else:
        n = []
        for i in range(0, len(string)):
            str_removed = string[:i] + string[i + 1 :]
            comb_next_iteration = generate_combinations(str_removed, r - 1)
            for element in comb_next_iteration:
                la = string[i] + element
                f = list(la)
                f.sort()
                f = "".join(f)
                if f not in n:
                    n.append(la)
    return n


def generate_permutations(string, r):
    if r == 1:
        perms = []
        for element in string:
            perms.append(element)
    else:
        perms = []
        for i in range(0, len(string)):
            str_removed = string[:i] + string[i + 1 :]
            comb_next_iteration = generate_permutations(str_removed, r - 1)
            for element in comb_next_iteration:
                perms.append(string[i] + element)
    return perms


def generate_cyclic_permutations(string):
    perm_var = generate_permutations(string, len(string))
    cyclic_permutations = []
    for item in perm_var:
        if cyclic_permutations:
            is_equal = False
            for cyclic_permutation in cyclic_permutations:
                for i in range(len(cyclic_permutation)):
                    cyclic_permutation = cyclic_permutation[1:] + cyclic_permutation[0]
                    if item == cyclic_permutation:
                        is_equal = True
            if (not is_equal) and (item not in cyclic_permutations):
                cyclic_permutations.append(item)
        else:
            cyclic_permutations.append(item)
    return cyclic_permutations


def multiset_p(multiset_of_strings):
    den = 1
    elements = []
    for element in multiset_of_strings:
        if element not in elements:
            elements.append(element)
            count_of_element = multiset_of_strings.count(element)
            den *= math.factorial(count_of_element)
    num = math.factorial(len([ed for ed in multiset_of_strings]))
    return num / den


def sigma(func, start, stop):
    ans = 0
    for i in range(start, stop + 1):
        ans = ans + func(i)
    return ans
