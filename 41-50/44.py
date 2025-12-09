from itertools import combinations as combs


def generate_primes(prime_nums: list[int]) -> list[int]:
    curr = prime_nums[-1] + 1
    is_prime = False
    while not is_prime:
        is_prime = True
        for j in range(2, curr - 1):
            if curr % j == 0:
                is_prime = False
                curr += 1
                break
    prime_nums.append(curr)
    return prime_nums


def get_prime_divs(n: int, prime_nums: list[int]) -> tuple[list[int], list[int]]:
    goal = n
    divisors = []
    index = 0
    curr_prime = 2
    while goal != 1:
        if curr_prime == prime_nums[-1]:
            prime_nums = generate_primes(prime_nums)
        if goal % curr_prime == 0:
            divisors.append(curr_prime)
            goal //= curr_prime
            index = 0
            curr_prime = 2
        else:
            index += 1
            curr_prime = prime_nums[index]
    return divisors, primes


def check_perfect_num(x: int, divisors: list[int]) -> int:
    n = len(divisors)
    vals = []
    for j in range(1, n + 1):
        for combination in combs(divisors, j):
            curr = 1
            for val in combination:
                curr *= val
            if curr not in vals:
                vals.append(curr)
    return True if sum(vals) - x == x else False


perfect_nums = []
i = 1
primes = [2]
while len(perfect_nums) < 4:
    divs_list, primes = get_prime_divs(i, primes)
    divs_list = [1] + divs_list
    if check_perfect_num(i, divs_list):
        perfect_nums.append(str(i))
    i += 1

print(f"Kod do bankoveho uctu riaditela banky je {''.join(perfect_nums)}")
