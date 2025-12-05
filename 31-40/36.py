file = open("36.input.txt", "r", encoding="UTF-8")

grades = {1: "Jeden", 2: "Dva", 3: "Tri", 4: "Styri", 5: "Pat"}
i = 0
sum = 0


print(33 * "_")
for line in file:
    i += 1
    line = line.strip().split()
    line[2] = int(line[2])
    sum += line[2]
    print(f"| {line[0]:<9}| {line[1]:<11}| {grades[line[2]]:<6}|")
    print(33 * "_")
print(f"|    priemer je {sum / i:.2f}            |")
print(33 * "_")
