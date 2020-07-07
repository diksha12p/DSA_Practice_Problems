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


if __name__ == '__main__':
    sol = Trie()
    words = ["anatomy", "ancestor", "anamoly", "anatomic"]
    for word in words:
        sol.insert(word)
    # sol.insert("anamoly")

    print(sol.search("anamoly"))
    print(sol.search("anamolous"))

    print(sol.starts_with("ana"))
    print(sol.starts_with("aya"))


