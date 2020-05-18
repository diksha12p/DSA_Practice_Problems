"""
LC 224. Basic Calculator - Hard
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        for ch in s:
            arr.append(ch)
        return self._calculate_util(arr)

    def _calculate_util(self, nums):
        stack, sign, num = [], '+', 0
        while len(nums) > 0:
            ch = nums.pop(0)

            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == '(':
                num = self._calculate_util(nums)
            if ch == '+' or ch == '-' or ch == ')' or len(nums) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                sign = ch
                num = 0
                if ch == ')':
                    break
        return sum(stack)
