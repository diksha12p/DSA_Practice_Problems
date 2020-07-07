"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            d[ch] = d.get(ch, 0) - 1
        return all(val == 0 for val in d.values())

    def isAnagram_space_op(self, s: str, t: str) -> bool:
        log = [0]* 26
        for ch in s:
            log[ord(ch) - ord('a')] += 1
        for ch in t:
            log[ord(ch) - ord('a')] -= 1
        return all(val == 0 for val in log)

    def isAnagram_sorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    sol = Solution()
    assert sol.isAnagram("anagram","nagaram") is True
    assert sol.isAnagram_counter("anagram", "nagaram") is True
    assert sol.isAnagram_sorted("anagram", "nagaram") is True
    assert sol.isAnagram_space_op("anagram", "nagaram") is True
