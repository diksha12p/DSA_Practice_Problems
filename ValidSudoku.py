"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

"""


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.row_check(board) and self.col_check(board) and self.sub_box_check(board)

    def row_check(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def col_check(self, board):
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        return True

    def sub_box_check(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                vals = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                if not self.is_valid(vals):
                    return False
        return True

    def is_valid(self, arr):
        arr = [ele for ele in arr if ele != '.']
        return len(arr) == len(set(arr))


if __name__ == '__main__':

    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    sol = Solution()
    print(sol.isValidSudoku(board))

