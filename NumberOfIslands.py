class Solution:
    #
    # def __init__(self, grid):
    #     self.rows = len(grid)
    #     self.cols = len(grid[0])
    #     self.grid = grid
    #
    #

    def numIslands(self, grid):
        if not grid:
            return 0

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "1":
                    self._DFS(i, j)
                    count += 1
        return count

    def _is_connected(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols and self.grid[i][j] == "1"

    def _DFS(self, i, j):
        self.grid[i][j] = "V"
        neighbour_row = [-1, 0, 0, 1]
        neighbour_col = [0, -1, 1, 0]

        for k in range(4):
            if self._is_connected(i + neighbour_row[k], j + neighbour_col[k]):
                #   Equivalent to calling self._DFS(i-1, j), self._DFS(i, j-1), self._DFS(i, j+1) and self._DFS(i+1, j)
                self._DFS(i + neighbour_row[k], j + neighbour_col[k])


    #     self.rows = len(grid)
    #     self.cols = len(grid[0])
    #     self.grid = grid
    #
    #     visited = [[False for j in range(self.cols)] for i in range(self.rows)]
    #     count = 0
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             if visited[i][j] == False and self.grid[i][j] == "1":
    #                 self._DFS(i,j,visited)
    #                 count += 1
    #     return count
    #
    # def _is_safe(self, i,j, visited):
    #     return 0 <= i < self.rows and 0 <= j < self.cols and not visited[i][j] and self.grid[i][j] == "1"
    #
    # def _DFS(self, i,j,visited):
    #     visited[i][j] = True
    #
    #     neighbour_row = [-1,  0, 0,  1]
    #     neighbour_col = [-0, -1, 1, 0]
    #
    #     for k in range(4):
    #         if self._is_safe(i + neighbour_row[k], j + neighbour_col[k], visited):
    #             self._DFS(i + neighbour_row[k], j + neighbour_col[k], visited)


graph = [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","","0","0"],
         ["1","1","0","0","0"]]
sol = Solution()
print(sol.numIslands(graph))