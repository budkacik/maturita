from random import randint as rnd

vals = [rnd(1, 1000) for x in range(150)]  # Vygeneruje Zźoznam pozostávajuci zo 150 náhodných čísel od 1 po 1000

first = 0
second = None

for val in vals:
    if val > first:
        second = first
        first = val
print(second)
