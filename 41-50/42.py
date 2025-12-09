from random import randint as rnd, choice as chc


def generate_dna_string() -> str:
    out = ""

    for _ in range(rnd(5, 15)):
        out += chc(["C", "T", "G", "A"])

    return out


for _ in range(5):
    print(generate_dna_string())
