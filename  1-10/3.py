from random import randint as rnd
num = rnd(1, 100)

while 1:
    try:
        guess = int(input("Zadaj cislo od 1 do 100 : "))

    except ValueError:
        print(f"zadaj cislo, napr. {rnd(1, 100)}")
        continue
    if guess < num:
        print("viac")
    elif guess > num:
        print("menej")
    else:
        print("Uhadol si cislo")
        break
