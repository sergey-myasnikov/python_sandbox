"""
3619. Count Islands With Total Value Divisible by K

You are given an m x n matrix grid and a positive integer k.
An island is a group of positive integers (representing land)
that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

Example 1:
    Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
    Output: 2
    Explanation:
        The grid contains four islands.
        The islands highlighted in blue have a total value that is divisible by 5,
        while the islands highlighted in red do not.

Example 2:
    Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
    Output: 6
    Explanation: The grid contains six islands, each with a total value that is divisible by 3.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 105
    0 <= grid[i][j] <= 106
    1 <= k <= 10^6

Source:
    https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/
"""

import doctest


def count_islands(grid: list[list[int]], k: int) -> int:
    """
    >>> count_islands([[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], 5)
    2
    >>> count_islands([[3,0,3,0], [0,3,0,3], [3,0,3,0]], 3)
    6
    """
    m, n = len(grid), len(grid[0])
    dirs = (-1, 0, 1, 0, -1)

    def dfs(i: int, j: int) -> int:
        total = grid[i][j]
        grid[i][j] = 0
        for d in range(4):
            x, y = i + dirs[d], j + dirs[d + 1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                total += dfs(x, y)
        return total

    return sum(
        grid[i][j] > 0 and dfs(i, j) % k == 0
        for i in range(m)
        for j in range(n)
    )

def count_islands_2(grid: list[list[int]], k: int) -> int:
    """
    >>> count_islands([[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], 5)
    2
    >>> count_islands([[3,0,3,0], [0,3,0,3], [3,0,3,0]], 3)
    6
    """
    m, n = len(grid), len(grid[0])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(i: int, j: int) -> int:
        total = grid[i][j]
        grid[i][j] = 0
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if x in range(m) and y in range(n) and grid[x][y] > 0:
                total += dfs(x, y)
        return total

    return sum(
        grid[i][j] > 0 and dfs(i, j) % k == 0
        for i in range(m)
        for j in range(n)
    )


if __name__ == "__main__":
    doctest.testmod()