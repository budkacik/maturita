from random import randint as rnd


def get_words() -> list[str] | None:
    inputs = input("zadaj vetu, kazde slovo musi mat aspon 4 znaky: ").strip().split()
    for inp in inputs:
        if len(inp) < 4:
            print("Musis zadat slovo ktore ma aspon 4 znaky")
            return
    return vals


def randomize_word(word: str) -> str:
    to_randomize = list(word[1:-1])
    out = word[0]
    for _ in range(len(to_randomize)):
        out += to_randomize.pop(rnd(0, len(to_randomize) - 1))
    return out + word[-1]


vals = get_words()
sentence = ""
for val in vals:
    sentence += randomize_word(val) + " "
print(sentence.strip())
