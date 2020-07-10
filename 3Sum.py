"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = []
        nums.sort()  # O(nlogn)
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, len(nums) - 1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif sum > 0: k -= 1
                    else: j += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.three_sum([-1, 0, 1, 2, -1, -4]))

