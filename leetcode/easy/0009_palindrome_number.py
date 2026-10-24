"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation:
        From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -2^31 <= x <= 2^31 - 1

Follow up:
    Could you solve it without converting the integer to a string?

Source:
    https://leetcode.com/problems/palindrome-number/
"""

import doctest

def is_palindrome_str(x: int) -> bool:
    """"
    >>> is_palindrome_str(121)
    True
    >>> is_palindrome_str(-121)
    False
    >>> is_palindrome_str(10)
    False
    """

    x_str = str(x)
    left, right = 0, len(x_str) - 1

    while left < right:
        if not x_str[left] == x_str[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome(x: int) -> bool:
    """"
    >>> is_palindrome(121)
    True
    >>> is_palindrome(-121)
    False
    >>> is_palindrome(10)
    False
    """

    if x < 0:
        return False

    reverse, xcopy = 0, x

    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10

    return reverse == xcopy


if __name__ == "__main__":
    doctest.testmod()