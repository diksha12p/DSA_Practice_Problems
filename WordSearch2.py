import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.ends_here = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.ends_here = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return False
        return node.ends_here

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if not node:
                return False
        return True


class Solution:
    def find_words(self, board, words):
        result, trie = [], Trie()
        node = trie.root

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, node, "", result)
        return result

    def dfs(self, board, i, j, curr_node, path, result):
        if curr_node.ends_here:
            result.append(path)
            curr_node.ends_here = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        temp = board[i][j]

        curr_node = curr_node.children.get(temp)
        if not curr_node:
            return

        board[i][j] = '#'

        self.dfs(board, i+1, j, curr_node, path+temp, result)
        self.dfs(board, i-1, j, curr_node, path+temp, result)
        self.dfs(board, i, j+1, curr_node, path+temp, result)
        self.dfs(board, i, j-1, curr_node, path+temp, result)

        board[i][j] = temp


if __name__ == '__main__':
    sol = Solution()
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    print(sol.find_words(board, words))

