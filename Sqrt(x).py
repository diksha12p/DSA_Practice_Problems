import math

"""
Boundary Variables: left = 0, right = x + 1 (and not x for cases when x = 0 or x = 1)
Condition: find minimal k such that k * k > x
Return Value: left - 1 (after exiting while loop, left is the minimal k satisfying the condition)
"""


class Solution:
    def square_root(self, x: int) -> int:

        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1


if __name__ == '__main__':
    sol = Solution()
    assert sol.square_root(1) == int(math.sqrt(1))
