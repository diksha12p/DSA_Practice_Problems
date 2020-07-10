"""
LC 463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and
there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a
square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the
island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if row == 0 or grid[row-1][col] == 0: peri += 1
                    if row == len(grid) - 1 or grid[row + 1][col] == 0: peri += 1
                    if col == 0 or grid[row][col - 1] == 0: peri += 1
                    if col == len(grid[0]) or grid[row][col + 1] == 0: peri += 1
        return peri


if __name__ == '__main__':
    sol = Solution()
    assert sol.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
