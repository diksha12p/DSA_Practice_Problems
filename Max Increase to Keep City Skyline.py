class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        matrix_row, matrix_col, final_result = [], [], []
        for row in grid:
            matrix_row.append(max(row))
        for col in zip(*grid):
            matrix_col.append(max(col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = min(matrix_row[i], matrix_col[j])

                if val != grid[i][j]:
                    final_result.append(val - grid[i][j])
        return sum(final_result)


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
sol = Solution()
print(sol.maxIncreaseKeepingSkyline(grid))