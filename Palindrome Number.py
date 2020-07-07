"""
LC 9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome_alt(self, x: int) -> bool:
        if x < 0:
            return False
        num , rev_num = x, 0
        while num:
            q, r = divmod(num, 10)
            rev_num = rev_num * 10 + r
            num = q
        return x == rev_num


if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False

    assert sol.isPalindrome_alt(121) is True
    assert sol.isPalindrome_alt(-121) is False
    assert sol.isPalindrome(10) is False
