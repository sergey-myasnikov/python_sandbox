""""
A Taylor series represents a function as an infinite sum of terms,
calculated from the values of its derivatives at a single point.

https://www.geeksforgeeks.org/engineering-mathematics/taylor-series/
"""

import math
from decimal import Decimal, getcontext

from Math.math_utils import get_e_error_percentage


def calc_e_taylor(iterations) -> float:
    """
    https://www.geeksforgeeks.org/dsa/program-to-efficiently-calculate-ex/

    Calculate e using Taylor series:
        e^x = 1 + x/1! + x^2/2! + x^3/3! + ...
        e = 1 + 1/1! + 1/2! + 1/3! + ...

    :param iterations: Number of terns to calculate
    :return: Approximate value of e
    """
    e_approx = 1.0
    factorial = 1.0

    for i in range(1, iterations):
        factorial *= i
        e_approx += 1.0 / factorial

    return e_approx

def calc_e_taylor_index_shift(iterations):
    """
    e approx = 163/60 + 1/6! + 1/7! + 1/8! + ...

    :param iterations: Number of terns to calculate
    :return: Approximate value of e
    """
    shift  = 6
    iterations += shift

    e_approx = 163 / 60
    factorial = 120  # 5!

    for i in range(shift, iterations):
        factorial *= i
        e_approx += 1.0 / factorial

    return e_approx

def calc_e_taylor_newton_brothers(iterations) -> float:
    """
    Accelerated convergence series for e
    or 'Newton brothers' e constant approximation

    e = Sun from 0 to infinity of (2n+2)/(2n+1)!

    :param iterations: Number of terns to calculate
    :return: Approximate value of e
    """

    getcontext().prec = 50

    e_approx = Decimal(0)
    for n in range(iterations):
        numerator = Decimal(2 * n + 2)
        denominator = Decimal(math.factorial(2 * n + 1))
        e_approx += numerator / denominator
    return float(e_approx)

def test_calc_e_taylor(func, iterations) -> None:

    for i in range(1, iterations + 1):
        e_approx = func(i)
        diff = get_e_error_percentage(e_approx)
        print(f"Iteration {i}: e = {e_approx}; accuracy = {diff} %")


if __name__ == "__main__":

    test_calc_e_taylor(calc_e_taylor, 15)
    test_calc_e_taylor(calc_e_taylor_index_shift, 10)
    test_calc_e_taylor(calc_e_taylor_newton_brothers, 10)