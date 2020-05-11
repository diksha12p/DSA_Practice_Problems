"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution:
    def isPerfectSquare_newton(self, num: int) -> bool:
        """
        Method 1: Using Newton's Method
        Let N be any number then the square root of N can be given by the formula:
        root = 0.5 * (X + (N / X))
        where X is any guess which can be assumed to be N or 1.
        """
        root = num
        while root * root > num:
            root = (root + (num/root)) // 2
        return root * root == num

    def isPerfectSquare_sum_of_odds(self, num: int) -> bool:
        """
        Method 1: Math trick by the sum of odd numbers
        Addition of first n odd numbers is always perfect square
        1 + 3 = 4,
        1 + 3 + 5 = 9,
        1 + 3 + 5 + 7 + 9 + 11 = 36 ...
        """
        i, curr_sum = 1, 0
        while  curr_sum < num:
            curr_sum += i
            if curr_sum == num:
                return True
            i += 2
        return False

    def isPerfectSum_binary_search(self, num):
        low, high = 0, num
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 == num:
                return True
            if mid ** 2 > num:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def isPerfectSum_linear_search(self, num):
        i = 1
        while i ** 2 <= num:
            if i ** 2 == num:
                return True
            else:
                i += 1
        return False

