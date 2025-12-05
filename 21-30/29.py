file = open("29.vstup.txt", "r", encoding="UTF-8")

months = {"Januar": [0, 0], "Februar": [0, 0], "Marec": [0, 0], "April": [0, 0], "Maj": [0, 0], "Jun": [0, 0], "Jul": [0, 0], "August": [0, 0], "September": [0, 0], "Oktober": [0, 0], "November": [0, 0], "December": [0, 0]}

for line in file:
    line = line.strip().split("|")
    line[2] = float(line[2])
    months[line[0]][0] += line[2]
    months[line[0]][1] += 1

for month in months:
    if months[month][0] == 0:
        continue
    print(f"{month}........\npriemerna cena: {months[month][0] / months[month][1]:.2f}\ncelkovy predaj: {months[month][0]:.2f}\n")
