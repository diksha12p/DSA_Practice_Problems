"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to
construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.


Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]


Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.


Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s: return []
        return self._util(s, wordDict, {})

    def _util(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s: return
        result = []
        for word in wordDict:
            if s.startswith(word):
                if len(s) == len(word):
                    result.append(word)
                else:
                    ans = self._util(s[len(word):], wordDict, memo)
                    for ele in ans:
                        result.append(word + ' ' + ele)
        memo[s] = result
        return result


if __name__ == '__main__':
    sol = Solution()

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    s1 = "pineapplepenapple"
    wordDict1 = ["apple", "pen", "applepen", "pine", "pineapple"]


    print(sol.wordBreak(s, wordDict))
    print(sol.wordBreak(s1, wordDict1))