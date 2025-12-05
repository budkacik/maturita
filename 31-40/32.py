val = input()


def check_palindrom(text: str) -> bool:
    for i in range(len(text) // 2):
        if text[i] != text[- 1 - i]:
            return False
    return True


print(val + (" je " if check_palindrom(val) else " nie je ") + "palindrom")
