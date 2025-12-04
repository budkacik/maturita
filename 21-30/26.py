from random import randint as rnd
import itertools
import threading
import time
import sys
global stop


def loading():
    for char in itertools.cycle(["", ".", "..", "..."]):
        if stop:
            break
        sys.stdout.write(f"\rGenerating values  {char}  ")
        sys.stdout.flush()
        time.sleep(0.5)


def linear_loading():
    for char in itertools.cycle(["", ".", "..", "..."]):
        if stop:
            break
        sys.stdout.write(f"\rLinear algorithm is working{char}")
        sys.stdout.flush()
        time.sleep(0.5)


def binary_loading():
    for char in itertools.cycle(["", ".", "..", "..."]):
        if stop:
            break
        sys.stdout.write(f"\rBinary algorithm is working{char}")
        sys.stdout.flush()
        time.sleep(0.5)


n = int(input("Zadaj cislo n: "))
x = int(input("Zadaj cislo x: "))
stop = False


loading_thread = threading.Thread(target=loading)
loading_thread.start()

nums = [rnd(0, 2 * x) for i in range(n)]
nums.append(x)
nums.sort()
nums = tuple(nums)

stop = True
loading_thread.join()
print("\nDone!\n")
stop = False


def linear_search(vals: list[int], num: int) -> int:
    for i in range(len(vals)):
        if vals[i] == num:
            return i


def binary_search(vals: list[int], num: int) -> int:
    current_index = len(vals) // 2
    depth = 1
    while 1:
        if vals[current_index] < num:
            current_index = current_index + current_index // 2 ** depth + 1
            if current_index >= len(vals):
                current_index = len(vals) - 1
        elif vals[current_index] > num:
            current_index = current_index // 2
        elif vals[current_index] == num:
            return [current_index, depth]
        depth += 1


loading_thread = threading.Thread(target=linear_loading)
loading_thread.start()
print(f"\nalgoritmus pre linearne vyhladavanie nasiel cislo {x} v zozname na indexe {linear_search(nums, x)}")
stop = True
loading_thread.join()
print("\nDone!\n")
stop = False


loading_thread = threading.Thread(target=binary_loading)
loading_thread.start()
bin = binary_search(nums, x)
print(f"\nalgoritmus pre binarne vyhladavanie nasiel cislo {x} v zozname na indexe {bin[0]}, pocet cyklov je {bin[1]}")
print(f"nums[{bin[0]}] = {nums[bin[0]]}")
stop = True
loading_thread.join()
print("\nDone!\n")
stop = False
