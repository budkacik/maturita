num = int(input())
vals = []
while 1:
    vals.append(num)
    num = input()
    if num == " ":
        break
    else:
        num = int(num)
print(sum(vals), len(vals), vals[-2])
