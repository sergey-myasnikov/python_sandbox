"""
Based on 'The Sum Over 1 Problem':
On average, how many random draws from the interval [0, 1] are necessary to ensure that their sum exceeds 1?

If you start generating random numbers between 0 and 1 and adding them up,
the average number of terms required for their sum to exceed 1 will be exactly e

"""

import random

from Math.math_utils import get_e_error_percentage


def calc_e_monte_carlo(simulations):

    total_numbers_picked = 0

    for _ in range(simulations):
        current_sum = 0
        count = 0
        while current_sum <= 1:
            current_sum += random.random()
            count += 1
        total_numbers_picked += count

    return total_numbers_picked / simulations

def test_calc_e_monte_carlo(iterations, simulations):
    for i in range(iterations):
        e_approx = calc_e_monte_carlo(simulations)
        diff = get_e_error_percentage(e_approx)
        print(f"Iteration {i}: e = {e_approx}; accuracy = {diff} %")


if __name__ == "__main__":

    test_calc_e_monte_carlo(3, 100_000)