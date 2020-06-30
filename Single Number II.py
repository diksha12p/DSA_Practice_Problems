"""
LC 137: Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3


Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
from typing import List


class Solution:
    def count_set_bits(self, nums: List[int]) -> int:
        result = 0

        # Iterate through every bit
        for i in range(0, 32):
            # Find sum of set bits at ith position in all array elements
            count, shift = 0, 1 << i
            for j in range(0, len(nums)):
                if nums[j] & shift:
                    count = count + 1

            # The bits with sum not multiple of 3, are the bits of element with single occurrence.
            if count % 3:
                result = result | shift

        return result

    def bit_manipulation(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for ele in nums:
            ones = (ones ^ ele) & (~twos)
            twos = (twos ^ ele) & (~ones)
        return ones


if __name__ == '__main__':
    sol = Solution()
    assert sol.bit_manipulation([2, 2, 3, 2]) == 3
    assert sol.count_set_bits([2, 2, 3, 2]) == 3
