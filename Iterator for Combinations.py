"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength
as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.result = []
        self.dfs(characters, "", combinationLength, 0)

    def next(self) -> str:
        if len(self.result):
            return self.result.pop(0)

    def hasNext(self) -> bool:
        return len(self.result) > 0

    def dfs(self, s, path, k, idx):
        if len(path) == k:
            self.result.append(path)
            return
        for i in range(idx, len(s)):
            self.dfs(s, path + s[i], k, i + 1)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
