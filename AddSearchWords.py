from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.ends_here = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            # if ch not in node.children:
            #     node.children[ch] = {}
            node = node.children[ch]
        node.ends_here = True

    def search(self, word):
        node = self.root
        self.result = False
        self._dfs(node, word)
        return self.result

    def _dfs(self, node, word):
        if not word:
            if node.ends_here:
                self.result = True
                print("Successful Search !")
            else:
                print("Unsuccessful Search !!")
            return

        if word[0] == '.':
            for nb in node.children.values():
                self._dfs(nb, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                print("Unsuccessful Search !!")
                return
            self._dfs(node, word[1:])



if __name__ == '__main__':
    word1 = "bad"
    word2 = "dad"

    obj = Trie()
    obj.insert(word1)
    obj.insert(word2)
    obj.search(word1)
    obj.search("Err")
    obj.search("b.d")






