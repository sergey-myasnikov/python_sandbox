"""
____________________
--- LEETCODE 509 ---
--------------------

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
    0 <= n <= 30

Source:
    https://leetcode.com/problems/fibonacci-number
"""

import doctest
import math
from functools import lru_cache


def fib(n):
    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(35)
    9227465
    >>> fib(100)
    354224848179261915075
    >>> fib(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    """
    one, two = 0, 1
    for i in range(n):
        one, two = (one + two), one
    return one


def fib_recursion(n):
    """
    Recursive approach is slow, works up to about 40

    >>> fib_recursion(0)
    0
    >>> fib_recursion(1)
    1
    >>> fib_recursion(2)
    1
    >>> fib_recursion(3)
    2
    >>> fib_recursion(4)
    3
    >>> fib_recursion(5)
    5
    >>> fib_recursion(6)
    8
    >>> fib_recursion(35)
    9227465
    """
    if n < 2:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_recursion_mem(n, seen):
    """
    Recursive with memoization is faster.
    Works up to 997. Then "RecursionError: maximum recursion depth exceeded in comparison" occurs.
    """
    if seen[n] != 0:
        return seen[n]

    if n < 2:
        return n

    result = fib_recursion_mem(n - 1, seen) + fib_recursion_mem(n - 2, seen)
    seen[n] = result
    return result


def fib_recursion_mem_run(n):
    """
    >>> fib_recursion_mem_run(0)
    0
    >>> fib_recursion_mem_run(1)
    1
    >>> fib_recursion_mem_run(2)
    1
    >>> fib_recursion_mem_run(3)
    2
    >>> fib_recursion_mem_run(4)
    3
    >>> fib_recursion_mem_run(5)
    5
    >>> fib_recursion_mem_run(6)
    8
    >>> fib_recursion_mem_run(35)
    9227465
    >>> fib_recursion_mem_run(100)
    354224848179261915075
    """
    seen = [0 for _ in range(n + 1)]
    return fib_recursion_mem(n, seen)


@lru_cache(maxsize=5)
def fib_recursion_cache(n):
    """
    Recursive approach with cache decorator.
    Works up to 997. Then "RecursionError: maximum recursion depth exceeded in comparison" occurs.

    >>> fib_recursion_cache(0)
    0
    >>> fib_recursion_cache(1)
    1
    >>> fib_recursion_cache(2)
    1
    >>> fib_recursion_cache(3)
    2
    >>> fib_recursion_cache(4)
    3
    >>> fib_recursion_cache(5)
    5
    >>> fib_recursion_cache(6)
    8
    >>> fib_recursion_cache(35)
    9227465
    >>> fib_recursion_cache(100)
    354224848179261915075
    """
    if n < 2:
        return n
    else:
        return fib_recursion_cache(n - 1) + fib_recursion_cache(n - 2)


def fib_bottom_up(n):
    """
    # Dynamic programming approach, similar to memoization and basic fib(n).
    Works fine for n >> 1000

    >>> fib_bottom_up(0)
    0
    >>> fib_bottom_up(1)
    1
    >>> fib_bottom_up(2)
    1
    >>> fib_bottom_up(3)
    2
    >>> fib_bottom_up(4)
    3
    >>> fib_bottom_up(5)
    5
    >>> fib_bottom_up(6)
    8
    >>> fib_bottom_up(35)
    9227465
    >>> fib_bottom_up(100)
    354224848179261915075
    >>> fib_bottom_up(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    """
    if n < 2:
        return n

    seen = [0 for _ in range(n + 1)]
    seen[0], seen[1] = 0, 1
    for i in range(2, n + 1):
        seen[i] = seen[i - 1] + seen[i - 2]
    return seen[-1]


def fib_binet(n):
    """
    Is presize up to n == 70
    >>> fib_binet(2)
    1
    >>> fib_binet(3)
    2
    >>> fib_binet(4)
    3
    >>> fib_binet(5)
    5
    >>> fib_binet(6)
    8
    >>> fib_binet(35)
    9227465
    >>> fib_binet(50)
    12586269025
    """
    sqrt5 = math.sqrt(5)
    return round((((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n) / sqrt5)


if __name__ == "__main__":
    doctest.testmod()
