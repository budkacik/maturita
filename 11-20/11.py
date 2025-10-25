from random import randint as rnd
val = input()
out = ""
for char in val:
    out += f"{chr(rnd(32, 126))}{char}{chr(rnd(32, 126))}"
print(out)
