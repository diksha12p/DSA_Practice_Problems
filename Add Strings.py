"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

1. The length of both num1 and num2 is < 5100.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

def add_strings(num1: str, num2: str) -> str:
    num1, num2 = list(num1), list(num2)
    carry, result = 0, []
    while len(num1) > 0 or len(num2) > 0:
        val1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
        val2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

        carry, val = divmod(val1 + val2 + carry, 10)
        result.append(str(val))
    if carry:
        result.append(str(carry))
    return ''.join(entry for entry in result[::-1])


if __name__ == '__main__':
    str1 = '121'
    str2 = '212'
    print(add_strings(str1, str2))
