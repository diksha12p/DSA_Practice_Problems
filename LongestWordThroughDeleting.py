"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
characters of the given string. If there are more than one possible results, return the longest word with the smallest
lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
"""


from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda e: (-len(e), e))
        for word in d:
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ""


if __name__ == '__main__':
    sol = Solution()

    assert sol.findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]) == "apple", "Incorrect Answer"
    assert sol.findLongestWord(s = "abpcplea", d = ["a", "b", "c"]) == "a", "Incorrect Answer"
