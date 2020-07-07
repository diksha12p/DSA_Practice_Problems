"""
LC 78: Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.gen_subsets(nums, 0, [], result)
        return result

    def gen_subsets(self, nums, curr_idx, curr, result):
        result.append(list(curr))
        # Iterating over all the elements of the array
        for i in range(curr_idx, len(nums)):
            # Include
            curr.append(nums[i])
            # Simulate proceeding while including it
            self.gen_subsets(nums, i + 1, curr, result)
            # Exclude
            curr.pop()

    def subsets_alt(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for ele in nums:
            result += [entry + [ele] for entry in result]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets_alt([1, 2, 3]))

