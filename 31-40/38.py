from random import randint as rnd

name = input("zadaj meno: ")
surname = input("zadaj priezvisko: ")


def generate_login(name1: str, name2: str) -> str:
    return f"{surname}.{name}"


def generate_password(name1: str, name2: str) -> str:
    complete = name1 + name2
    out = ""

    for _ in range(8):
        curr = all[rnd(0, len(all) - 1)].lower()
        if rnd(0, 1) == 1:
            curr = curr.upper()
        out += curr
    rand_index = rnd(0, 7)
    return out[:rand_index] + str(rnd(0, 9)) + out[rand_index + 1:]


print(f"toto je login: {generate_login(name, surname)}\ntoto je heslo: {generate_password(name, surname)}")
