def get_fizz():
    return "Fizz"


def get_buzz():
    return "Buzz"


def get_fizz_buzz():
    return f"{get_fizz()}{get_buzz()}"


def is_divisible_by_3(number: int) -> bool:
    return (number % 3) == 0


def is_divisible_by_5(number: int) -> bool:
    return (number % 5) == 0


def is_divisible_by_3_and_5(number: int) -> bool:
    return is_divisible_by_3(number) and is_divisible_by_5(number)


def fizz_buzz(number: int) -> str:
    if is_divisible_by_3_and_5(number):
        return get_fizz_buzz()
    elif is_divisible_by_3(number):
        return get_fizz()
    elif is_divisible_by_5(number):
        return get_buzz()
    else:
        return str(number)
