"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not
connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:

Input: A = [[0,1],[1,0]]
Output: 1


Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2


Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""
from typing import List


# ERROR: TLE || Check class 'Solution'
class Solution1:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        setA, setB = set(), set()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                if not len(setA):
                    self.flood_fill(setA, A, i, j)
                    print("Set A {}".format(setA))
                elif not len(setB) and (i,j) not in setA:
                    self.flood_fill(setB, A, i, j)
                    print("Set B {}".format(setB))

        ans = m+n
        for a in setA:
            for b in setB:
                # abs(a[0] - b[0]) + abs(a[1] - b[1]) - 1
                ans = min(ans, abs(a[0] - b[0]) + abs(a[1] - b[1]) - 1)
        return ans

    def flood_fill(self, curr_set, A, x, y):
        curr_set.add((x,y))

        nb_x = (0, 0, 1, -1)
        nb_y = (1, -1, 0, 0)

        for i in range(4):
            nx = x + nb_x[i]
            ny = y + nb_y[i]
            if 0 <= nx < len(A) and 0 <= ny < len(A[0]):
                if A[nx][ny] == 1 and (nx,ny) not in curr_set:
                    self.flood_fill(curr_set, A, nx, ny)


class Solution:
    def paint(self, A, i, j):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]) or A[i][j] == 0 or A[i][j] == 2:
            return
        A[i][j] = 2
        for nb in [(0,1),(0,-1),(1,0),(-1,0)]:
            self.paint(A, i + nb[0], j + nb[1])

    def expand(self, A, i, j, color):
        if i >= len(A) or i < 0 or j < 0 or j >= len(A[0]):
            return False
        if A[i][j] == 0:
            A[i][j] = color + 1
        return A[i][j] == 1

    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m, n, flag = len(A), len(A[0]), False
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if A[i][j] == 1:
                    self.paint(A, i, j)
                    flag = True
                    break

        for color in range(2, 2+m+n+1):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == color and ( self.expand(A, i-1, j, color) or self.expand(A, i, j+1, color) or
                                              self.expand(A, i+1, j, color) or self.expand(A, i, j-1, color)):
                        return color-2


if __name__ == '__main__':
    sol = Solution()
    # print(sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
    print(sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))



