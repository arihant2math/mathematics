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


def prime_gen(stop, start=1, want_list=True):
    """Generates primes from start=>stop"""
    if start is None:
        start = 1
    if want_list:
        ans = []
        for i in range(start, stop):
            if is_prime(i):
                ans.append(i)
        return ans
    else:
        for i in range(start, stop):
            if is_prime(i):
                print(i)


def mersenne(n):
    """
    Returns the mersenne of the number ((2**n)-1)
    :param n:
    :return:
    """
    return (2 ** n) - 1


def lucas_lehmer(n):
    """Implements Lucas Lehmer mersenne prime test."""
    m = mersenne(n)
    lucas_lehmer_list = [4]
    if len(lucas_lehmer_list) < n:
        for num in range(n - 1):
            lucas_lehmer_list.append(lucas_lehmer_list[-1] ** 2 - 2)
    if lucas_lehmer_list[n - 1] == 0:
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
    ans = []
    for i in range(2, number):
        if is_prime(i):
            x = 0
            while x == 1:
                if number % i == 0:
                    ans.append(i)
                    number = int(number / i)
                else:
                    x = 2
            if number == 1:
                return ans


def factor(number):
    return [
        i for i in range(1, number + 1) if not number % i
    ]


def step_in_euclidean_algorithm(a, b):
    x, y = divmod(a, b)
    return a, b, x, y


def euclidean_algorithm(a, b, want_fancy):
    li = step_in_euclidean_algorithm(a, b)
    while li[3] != 0:
        li = step_in_euclidean_algorithm(li[1], li[3])
    if want_fancy:
        return str(li[0]) + " = " + str(li[1]) + "(" + str(li[2]) + ")" + "+" + str(li[3])
    else:
        return li


# def extended_euclidean_algorithm():
#     # should have param number
#     return NotImplemented


def repeated_squaring(number, power):
    ans = 1
    for i in range(power):
        ans *= number
    print(ans)


def find_lcm(m, n):
    result = m * n / math.gcd(m, n)
    print(result)


def totient_function(m, print_units):
    units = [i for i in range(1, m + 1) if math.gcd(i, m) == 1]
    ans = len(units)
    if print_units:
        return ans, units
    else:
        return ans


def nth_power(stop, power):
    return [
        i ** power for i in range(1, stop + 1)
    ]


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
    return "none"


def primitive_root_table_multiplication(modulus):
    modulus = int(modulus)
    name = "primitive_root_table" + str(modulus) + ".txt"
    file = open(name, 'w')
    file.write(
        '\\documentclass{article}\n' + '\\usepackage[utf8]{inputenc}\n' + '\\begin{document}\n' +
        '\\begin{tabular}{|c|c|}\n' + 'number & primitive root equivalent \\ \n')
    primitive_roots = primitive_root(modulus)
    two_gens = False
    list_of_numbers = {}
    if "," in str(primitive_roots):
        two_gens = True
    if two_gens:
        for w, x, y, z in itertools.product(range(1, modulus, 2), repeat=4):
            if pow(int(w), int(x)) * pow(y, z) % int(modulus) not in list_of_numbers:
                list_of_numbers.update({str(w) + " " + str(x) + " " + str(y) + " " + str(z): (pow(w, x) * pow(y, z))})
        for key in list_of_numbers:
            w = x = y = z = 0
            var = ""
            for item in key:
                if item == " ":
                    if w == 0:
                        w = var
                    elif x == 0:
                        x = var
                    elif y == 0:
                        y = var
                    elif z == 0:
                        z = var
                    var = ""
                else:
                    var = var + item
            new_key = "$" + str(w) + "^" + str(x) + "\\cdot" + str(y) + "^" + str(z) + "$"
            line = new_key + " & " + "$" + str(modulus) + "^" + str(list_of_numbers[key]) + "$"
            line = line + '\\ ' + '\n'
            file.write(line)
    else:
        for i in range(1, modulus):
            list_of_numbers.update({"$" + str(i) + "$": "$" + str(primitive_roots) + "^" + str(i) + "$"})
    file.write('\\end{tabular}\n' + '\\end{document}\n')
    file.close()


def root_equivalents(modulus, square_of_root):
    return [i for i in range(0, modulus) if i ** 2 % modulus == square_of_root]


def sum_set_exploration(set_a, set_b):
    sum_set = []
    for a in set_a:
        for b in set_b:
            sum_set.append(a + b)
    sum_set = set(sum_set)
    return sum_set


def pigeon_hole(colors, number_needed):
    return (number_needed - 1) * colors
