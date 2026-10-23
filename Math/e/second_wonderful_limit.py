from decimal import Decimal, getcontext

from Math.math_utils import get_e_error_percentage


def calc_e_limit(x) -> float:
    """
    Calculate e using the second wonderful limit
    e = limit of(1 + 1/x)^x as x approaches the infinity

    :param x: x approaching the infinity
    :return: Approximate value of e
    """

    return (1 + (1 / x)) ** x

def test_calc_e_limit_1(iterations) -> None:
    for i in range(1, iterations + 1):
        e_approx = calc_e_limit(i)
        diff = get_e_error_percentage(e_approx)
        print(f"Iteration {i}: e = {e_approx}; accuracy = {diff} %")

def test_calc_e_limit_2() -> None:
    """
    Uncover the accuracy limit.
    For large values of x floating point number 1/x is rounded to 0.0
    """
    iterations = (10, 100_000, 10_000_000, 10**16)
    last_diff = 0
    for i in iterations:
        e_approx = calc_e_limit(i)
        diff = get_e_error_percentage(e_approx)
        print(f"Iteration {i}: e = {e_approx}; accuracy = {diff} %; "
              f"Accuracy {'increased' if diff > last_diff else 'DECREASED'}")
        last_diff = diff


def calc_e_limit_decimal(x) -> float:
    getcontext().prec = 30
    i = Decimal(x)
    return float((Decimal('1') + Decimal('1') / i) ** i)

def test_calc_e_limit_decimal() -> None:
    for i in range(15, 26):
        e_approx = calc_e_limit_decimal(10**i)
        diff = get_e_error_percentage(e_approx)
        print(f"Iteration 10**{i}: e = {e_approx}; accuracy = {diff} %")


if __name__ == "__main__":

    test_calc_e_limit_1(100)
    test_calc_e_limit_2()
    test_calc_e_limit_decimal()