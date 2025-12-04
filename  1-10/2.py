distance = int(input())


def get_price(distance_: int) -> float:
    if distance_ <= 10:
        return 0.50
    elif distance_ <= 20:
        return 0.45
    elif distance_ <= 30:
        return 0.40
    else:
        return 0.35


def jazdne(kilometre: int, cena_km: float) -> str:
    return f"cena je {kilometre * cena_km:.02f}"


print(jazdne(distance, get_price(distance)))
