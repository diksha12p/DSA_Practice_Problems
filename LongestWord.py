from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def longest_word(self):
        def _helper(node, partial_res):
            result = partial_res
            for ch, child in node.children.items():
                if child.end:
                    potential_res = _helper(child, partial_res + ch)
                    if (len(potential_res) > len(result)) or (
                            len(potential_res) == len(result) and potential_res < result):
                        result = potential_res
            return result

        return _helper(self.root, '')


# Method 1: Trie + DFS
class Solution:
    def longestWord(self, words: List[str]) -> str:
        T = Trie()
        for word in words:
            T.insert(word)
        return T.longest_word()


# Method 2: Sort beforehand and check for each 'word' in the input 'words'
def longestWord(words):
    word_set = set(words)
    # print(word_set)
    words.sort(key=lambda c: (-len(c), c))
    # print(words)
    for word in words:
        if all(word[:k] in word_set for k in range(1, len(word))):
            return word

    return ""


if __name__ == '__main__':
    print("OUTPUT 1:    ", longestWord(["w","wo","wor","worl", "world"]))

    sol = Solution()
    print("OUTPUT 2:    ", sol.longestWord(["w","wo","wor","worl", "world"]))