"""
Implement atoi which converts a string to an integer.


The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

INFERENCE -->> Strip all whitespace until first non-whitespace char



The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

INFERENCE -->> Ignore non digit chars after or in between digits

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

INFERENCE -->> First non-whitespace char is non integer, return 0

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values,
INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.


INFERENCE -->> INT_MIN < result < INT_MAX

Example 1:
Input: "42"
Output: 42


Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.


Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.


Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.


Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Therefore INT_MIN (−231) is returned.

"""


class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        str = str.strip()
        if not str:
            return 0
        result = 0
        sign = -1 if str[0] is '-' else 1
        if str[0] in ['+', '-']:
            str = str[1:]
        for i in range(len(str)):
            if not str[i].isdigit():
                break
            result = result*10 + int(str[i])
            if result > INT_MAX:
                break
        return min(max(sign * result, INT_MIN), INT_MAX)


if __name__ == '__main__':
    atoi = Solution()
    gen_output, exp_output = [], [42, -42, -2147483648, 0, 4193, 0, 3, 0, 1]

    test = ["42", "   -42", "-91283472332", "words and 987", "4193 with words", "test case 41#22", "3.14159", "+", "+1"]
    for input in test:
        gen_output.append(atoi.myAtoi(input))

    assert gen_output == exp_output

