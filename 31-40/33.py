def shift_char(vals: list[int], m: int) -> list[int]:
    outord = []
    for i in range(len(vals)):
        if vals[i] == 32:
            outord.append(vals[i])
        elif 65 <= vals[i] <= 90:
            if vals[i] + m > 90:
                outord.append(vals[i] + m - 26)
            elif vals[i] + m < 65:
                outord.append(vals[i] + m + 26)
            else:
                outord.append(vals[i] + m)
        else:
            if vals[i] + m > 122:
                outord.append(vals[i] + m - 26)
            elif vals[i] + m < 97:
                outord.append(vals[i] + m + 26)
            else:
                outord.append(vals[i] + m)
    return outord


def encode(text: str, n: int) -> str:
    ords = []
    for i in text:
        ords.append(ord(i))
    vals = shift_char(ords, n)
    out = ""
    for i in range(len(vals)):
        out += chr(vals[i])
    return out


def decode(text: str, n: int) -> str:
    ords = []
    for i in text:
        ords.append(ord(i))
    vals = shift_char(ords, n)
    out = ""
    for i in range(len(vals)):
        out += chr(vals[i])
    return out


user_string = input("zadaj retazed na zakodovanie: ")
shift = int(input("zadaj hodnotu posunu pismen: "))
encoded = encode(user_string, shift)
print(f"\ntoto je zakodovany retazec: {encoded}\ntoto je dekodovany retazec: {decode(encoded, -shift)}")
decoded = decode(encoded, -1)
print(encoded)
