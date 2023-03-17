from fizz_buzz import fizz_buzz, get_fizz, get_buzz, get_fizz_buzz, number_to_string


def test_get_fizz_should_return_the_string_fizz() -> None:
    assert get_fizz() == "Fizz"


def test_get_buzz_should_return_the_string_buzz() -> None:
    assert get_buzz() == "Buzz"


def test_get_fizz_buzz_should_return_the_string_fizzbuzz() -> None:
    assert get_fizz_buzz() == "FizzBuzz"


def test_number_to_string_should_return_the_string_2_when_number_is_2() -> None:
    assert number_to_string(2) == "2"


def test_fizz_buzz_should_return_the_string_1_when_number_is_1() -> None:
    assert fizz_buzz(1) == "1"


def test_fizz_buzz_should_return_the_string_fizz_when_number_is_3() -> None:
    assert fizz_buzz(3) == get_fizz()


def test_fizz_buzz_should_return_the_string_buzz_when_number_is_5() -> None:
    assert fizz_buzz(5) == get_buzz()


def test_fizz_buzz_should_return_the_string_fizzbuzz_when_number_is_15() -> None:
    assert fizz_buzz(15) == get_fizz_buzz()
