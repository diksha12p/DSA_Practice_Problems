"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, options, path, result):
        if not options:
            result.append(path)
        for i in range(len(options)):
            self.dfs(options[:i] + options[i + 1:], path + [options[i]], result)


if __name__ == '__main__':
    sol = Solution()
    exp_output = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    assert sol.permute([1,2,3]) == exp_output
