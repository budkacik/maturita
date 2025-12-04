file = open("51.txt", "r")
sum = 0


def space_generator(n):
    return " " * n


block = (10, 10, 10, 9)
first_line = ("tovar", "mnozstvo", "cena", "celkom")
print(f"{first_line[0]}{space_generator(block[0] - len(first_line[0]))}{first_line[1]}{space_generator(block[1] - len(first_line[1]))}{first_line[2]}{space_generator(block[2] - len(first_line[2]))}{first_line[3]}")
print(block[0] * "*" + block[1] * "*" + block[2] * "*" + block[3] * "*")

for line in file:
    line = line.strip().split()
    item = (line[0], f"{float(line[1]):.2f}", f"{float(line[2]):.2f}")
    print(f"{item[0]}{space_generator(block[0] - len(item[0]))}{item[1]}{space_generator(block[1] - len(item[1]))}{item[2]}{space_generator(block[2] - len(item[2]))}{float(line[1]) * float(line[2]):.2f} EUR")
    sum += float(line[1]) * float(line[2])

file.close()
last_line = ("SPOLU:", "", f"{sum:.2f} EUR")

print(block[0] * "*" + block[1] * "*" + block[2] * "*" + block[3] * "*")
print(f"{last_line[0]}{space_generator(block[0] - len(last_line[0]))}{last_line[1]}{space_generator(block[1] - len(last_line[1]))}{last_line[1]}{space_generator(block[2] - len(last_line[1]))}{last_line[2]}")

