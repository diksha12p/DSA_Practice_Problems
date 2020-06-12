"""
LC 542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:

Input:                       Output:

[[0,0,0],                   [[0,0,0],
 [0,1,0],       ====>        [0,1,0],
 [0,0,0]]                    [0,0,0]]


Example 2:

Input:                       Output:

[[0,0,0],                   [[0,0,0],
 [0,1,0],       ====>        [0,1,0],
 [1,1,1]]                    [1,2,1]]

"""
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.bfs(matrix, i, j)
        return matrix

    def bfs(self, matrix, x, y):
        queue = [(x, y, 0)]  # (x: x coordinate, y: y coordinate, 0: step number)
        while queue:
            # print(queue)
            i, j, curr_step = queue.pop(0)
            for nb_x, nb_y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nb_x < len(matrix) and 0 <= nb_y < len(matrix[0]):
                    if matrix[nb_x][nb_y] == 0:
                        matrix[x][y] = curr_step + 1
                        return
                    else:
                        queue.append((nb_x, nb_y, curr_step + 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
