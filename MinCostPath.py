class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        # start = grid[0][0]
        m, n = len(grid) - 1, len(grid[0]) - 1
        self._min_path_util(grid,m,n)
        # target = grid[len(grid)-1][len(grid[0])-1]

    def _min_path_util(self,grid,m,n):
        if n < 0 or m < 0:
            return 0
        elif m == 0 and n == 0:
            return grid[m][n]
        else:
            return grid[len(grid) - 1][len(grid[0]) - 1] + self._min(self._min_path_util(grid, m - 1, n - 1),
                                                                     self._min_path_util(grid, m - 1, n),
                                                                     self._min_path_util(grid, m, n - 1))

    def _min(self, x, y, z):
        if x < y:
            return x if (x < z) else z
        else:
            return y if (y < z) else z


cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
sol = Solution()
print(sol.minPathSum(cost))