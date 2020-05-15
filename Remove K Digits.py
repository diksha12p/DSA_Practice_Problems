"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the
smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # IDEA: Remove the element from L to R if it causes a dip i.e. greater than the next element
        for char in num:
            while k and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)

        # Num is already in an increasing order -> Stack has the same numbers
        while k:
            stack.pop()
            k -= 1

        # Retrieving the number from the entries in stack
        # or '0'ensures that something is returned in case stack in empty
        return ''.join(stack).lstrip('0') or '0'


sol = Solution()
print(sol.removeKdigits('10', 2))



