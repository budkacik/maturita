from collections import deque


def generate_primes(prime_nums: list[int]) -> list[int]:
    curr = prime_nums[-1] + 1
    is_prime = False
    while not is_prime:
        is_prime = True
        for i in range(2, curr - 1):
            if curr % i == 0:
                is_prime = False
                curr += 1
                break
    prime_nums.append(curr)
    return prime_nums


def get_primes_list(n: int) -> list[int]:
    primes = [1, 2]
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    while 1:
        if n < primes[-1]:
            return primes[:-1]
        else:
            primes = generate_primes(primes)


def pretty_print(vals: list[int]) -> str:
    max_len = len(str(vals[-1]))
    vals = deque(vals)
    out = ""

    if max_len >= 60:
        while max_len >= 60:
            out += str(vals.pop()) + "\n"
            max_len = len(str(vals[-1]))

    while vals:
        line_len = 0
        full = False

        while not full:
            curr = vals.pop()
            out += str(curr) + " "
            line_len += len(str(curr)) + 1
            if line_len >= 100 or not vals:
                full = True
                out += "\n"
    return out


print(pretty_print(get_primes_list(int(input("zadaj cislo N: ")))))
