from typing import List

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word, visited):
                    return True
        return False

    def dfs(self, board, i, j, count, word, visited):
        if count == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count] or visited.get((i, j)):
            return False

        visited[(i, j)] = True

        was_found = self.dfs(board, i+1, j, count+1, word, visited) or self.dfs(board, i-1, j, count+1, word, visited) \
                    or \
                    self.dfs(board, i, j+1, count+1, word, visited) or self.dfs(board, i, j-1, count+1, word, visited)

        visited[(i, j)] = False

        return was_found


sol = Solution()
board_user = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(sol.exist(board_user, "ABCCED"))


