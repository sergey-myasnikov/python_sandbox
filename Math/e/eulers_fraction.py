"""
Euler's Continued Fraction

Leonhard Euler himself discovered that the number e can be expanded into
an infinite continued fraction with a surprisingly strict structure:

e = 2 + 1 / (1 + 1 / (2 + 1 / (1 + 1 / (1 + 1 / (4 + 1 / ...)))))

"""

from Math.math_utils import get_e_error_percentage


def calc_e_continued_fraction(depth):

    # Generate Euler's sequence for the given depth
    seq = [2]
    for i in range(1, depth):
        if i % 3 == 2:
            seq.append(2 * (i // 3 + 1))
        else:
            seq.append(1)

    # Calculate the fraction from the bottom up
    result = 0
    for x in reversed(seq[1:]):
        result = 1 / (x + result)

    return seq[0] + result

def test_calc_e_continued_fraction(iterations):
    for i in range(1, iterations):
        e_approx = calc_e_continued_fraction(i)
        diff = get_e_error_percentage(e_approx)
        print(f"Depth {i}: e = {e_approx}; accuracy = {diff} %")


if __name__ == "__main__":
    test_calc_e_continued_fraction(30)