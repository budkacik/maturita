file = open("28.vety.txt", "r", encoding="UTF-8")

long = 0
i = 1

for line in file:
    if len(line) > long:
        long = len(line)
        target = i
    i += 1

print(f"najdlhsia veta je na riadku {target}\n")

file = open("28.vety.txt", "r", encoding="UTF-8")
samohlasky = "AÁIÍYÝEÉUÚOÓaáäiíyýeéuúoóô"

for line in file:
    out = ""
    for char in line:
        out += char if char not in samohlasky else "*"
    print(out.strip())
