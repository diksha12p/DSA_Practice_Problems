"""
Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed
from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that
sequence should now be considered adjacent to each other. This process should be repeated as many time as possible.
You should greedily remove characters from left to right.

Example 1:
Input: "aaabbbc"
Output: "c"
Explanation:
1. Remove 3 'a': "aaabbbc" => "bbbc"
2. Remove 3 'b': "bbbc" => "c"


Example 2:
Input: "aabbbacd"
Output: "cd"
Explanation:
1. Remove 3 'b': "aabbbacd" => "aaacd"
2. Remove 3 'a': "aaacd" => "cd"


Example 3:
Input: "aabbccddeeedcba"
Output: ""
Explanation:
1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
3. Remove 3 'c': "aabbcccba" => "aabbba"
4. Remove 3 'b': "aabbba" => "aaa"
5. Remove 3 'a': "aaa" => ""


Example 4:
Input: "aaabbbacd"
Output: "acd"
Explanation:
1. Remove 3 'a': "aaabbbacd" => "bbbacd"
2. Remove 3 'b': "bbbacd" => "acd"
"""


def candy_crush(input: str) -> str:
    if not input:
        return input
    stack = [[input[0], 1]]
    for i in range(1, len(input)):
        if stack[-1][0] == input[i]:
            stack[-1][1] += 1
        else:
            if stack and stack[-1][1] >= 3:
                stack.pop(-1)
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            else:
                stack.append([input[i], 1])

    if stack and stack[-1][1] >= 3:
        stack.pop(-1)
    return ''.join([ele*count for ele, count in stack])


if __name__ == '__main__':

    assert candy_crush("aaaabbbc") == 'c', "Incorrect Code"
    assert candy_crush("aabbbacd") == 'cd', "Incorrect Code"
    assert candy_crush("aabbccddeeedcba") == '', "Incorrect Code"
    assert candy_crush("aabbbaacd") == 'cd', "Incorrect Code"
    assert candy_crush("dddabbbbaccccaax") == 'x', "Incorrect Code"

