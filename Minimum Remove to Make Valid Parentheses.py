"""
LC 1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"


Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, d, result = [], {}, []

        # Loop 1: Identifying and logging indices for valid parenthesis
        for idx,ele in enumerate(s):
            if ele == '(':
                stack.append(idx)
            elif ele == ')' and stack:
                d[idx] = True
                d[stack[-1]] = True
                stack.pop()

        # Loop 2: Appending only the valid parenthesis i.e. for which d[idx] == True, to the list
        for idx,ele in enumerate(s):
            if ele == ')' or ele == '(':
                if idx in d:
                    result.append(ele)
            # Every other character except parenthesis
            else:
                result.append(ele)
        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    assert (sol.minRemoveToMakeValid("lee(t(c)o)de)")) == 'lee(t(c)o)de', "Incorrect Code"
    assert (sol.minRemoveToMakeValid("a)b(c)d")) == "ab(c)d", "Incorrect Code"
    assert (sol.minRemoveToMakeValid("))((")) == '', "Incorrect Code"
    assert (sol.minRemoveToMakeValid("(a(b(c)d)")) == 'a(b(c)d)', "Incorrect Code"



