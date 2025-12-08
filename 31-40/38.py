from random import randint as rnd

name = input("zadaj meno: ")
surname = input("zadaj priezvisko: ")

login = f"{surname}.{name}"
passw = ""

all = name + surname

for _ in range(8):
    curr = all[rnd(0, len(all) - 1)].lower()
    if rnd(0, 1) == 1:
        curr = curr.upper()
    passw += curr
rand_index = rnd(0, 7)
passw = passw[:rand_index] + str(rnd(0, 9)) + passw[rand_index + 1:]

print(f"toto je login: {login}\ntoto je heslo: {passw}")
