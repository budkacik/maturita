a = int(input())
b = int(input())
primes = [2]


def generate_primes(primes: list) -> list:
    curr = primes[-1] + 1
    is_prime = False
    while not is_prime:
        is_prime = True
        for i in range(2, curr - 1):
            if curr % i == 0:
                is_prime = False
                curr += 1
                break
    primes.append(curr)
    return primes


def get_prime_divs(n, primes):
    goal = n
    divisors = []
    index = 0
    curr_prime = 2
    while goal != 1:
        if curr_prime == primes[-1]:
            primes = generate_primes(primes)
        if goal % curr_prime == 0:
            divisors.append(curr_prime)
            goal //= curr_prime
            index = 0
            curr_prime = 2
        else:
            index += 1
            curr_prime = primes[index]
    return [n, primes, divisors]


def nsd(divs1, divs2, num1, num2):
    divisor = 1
    for i in range(len(divs1)):
        for j in range(len(divs2)):
            if divs1[i] == divs2[j] and divs1[i] != None:
                divisor *= divs1[i]
                divs1[i] = None
                divs2[j] = None
    return divisor

a_vals = get_prime_divs(a, primes)
b_vals = get_prime_divs(b, a_vals[1])
print(a_vals[2], b_vals[2])
print(nsd(a_vals[2], b_vals[2], a_vals[0], b_vals[0]))
