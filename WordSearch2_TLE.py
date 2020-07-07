from typing import List


class Solution_TLE:
    # Standard DFS search in a 2D matrix -> TLE
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = list()
        for word in words:
            if self.exist(board, word):
                output.append(word)
        return output

    def exist(self, board: List[List[str]], word: str) -> bool:
        # visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
        return False

    def dfs(self, board, i, j, count, word):
        if count == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        was_found = self.dfs(board, i+1, j, count+1, word) or self.dfs(board, i-1, j, count+1, word) \
                    or \
                    self.dfs(board, i, j+1, count+1, word) or self.dfs(board, i, j-1, count+1, word)

        board[i][j] = temp

        return was_found


if __name__ == '__main__':
    sol = Solution_TLE()
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    print(sol.findWords(board, words))

