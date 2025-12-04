from math import inf
file = open("ziaci.txt", "r", encoding="UTF-8")
names = []
surnames = []
ages = []
for line in file:
    line = line.strip().split()
    names.append(line[0])
    surnames.append(line[1])
    ages.append(int(line[2]))
file.close()

age_max = -inf

for i in range(len(ages)):
    if ages[i] > age_max:
        age_max = ages[i]
        index = i

print(f"Najstarsi ziak sa vola {names[index]} {surnames[index]} a ma {age_max} rokov")
print(f"Priemerny vek ziakov je {sum(ages) / len(ages):.1f}")

file = open("8.output.txt", "w", encoding="UTF-8")
for i in range(len(ages)):
    if ages[i] < 19:
        file.write(f"{names[i]} {surnames[i]} {ages[i]}\n")
