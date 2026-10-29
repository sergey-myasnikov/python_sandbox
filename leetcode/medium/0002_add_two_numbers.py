"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

Source:
    https://leetcode.com/problems/add-two-numbers/
"""

import doctest

from typing import Optional

from leetcode.common import ListNode


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]):
    """
    >>> l1 = ListNode(2, ListNode(4, ListNode(3)))
    >>> l2 = ListNode(5, ListNode(6, ListNode(4)))
    >>> cur = add_two_numbers(l1, l2)
    >>> while cur:
    ...     print(cur.val)
    ...     cur = cur.next
    7
    0
    8
    >>> l1 = ListNode(0)
    >>> l2 = ListNode(0)
    >>> cur = add_two_numbers(l1, l2)
    >>> while cur:
    ...     print(cur.val)
    ...     cur = cur.next
    0
    >>> l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    >>> l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    >>> cur = add_two_numbers(l1, l2)
    >>> while cur:
    ...     print(cur.val)
    ...     cur = cur.next
    8
    9
    9
    9
    0
    0
    0
    1
    """

    dummy = ListNode()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10

        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == '__main__':
    doctest.testmod()