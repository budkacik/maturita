def generate_spaces(item: str) -> str:
    return (6 - len(item)) * " "


out = "1"
for i in range(2, 21):
    out += generate_spaces(str(i)) + str(i)
print(out)

out = "1"
for i in range(2, 21):
    out += generate_spaces(f"{i:b}") + f"{i:b}"
print(out)

out = "1"
for i in range(2, 21):
    out += generate_spaces(f"{i:x}") + f"{i:x}"
print(out)
