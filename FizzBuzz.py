"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        if n < 3:
            return [str(num) for num in range(1, n + 1)]
        for num in range(1, n + 1):
            if not num % 3 and not num % 5:
                result.append("FizzBuzz")
            elif not num % 3:
                result.append("Fizz")
            elif not num % 5:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result

    def fizzbuzz_op(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if not i % 3 or not i % 5:
                result.append('Fizz' * (not i % 3) + 'Buzz' * (not i % 5))
            else:
                result.append(str(i))
        return result

    def fizzbuzz_alt(self, n: int) -> List[str]:
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


if __name__ == '__main__':
    sol = Solution()
    assert (sol.fizzBuzz(15)) == (sol.fizzbuzz_op(15)) == (sol.fizzbuzz_alt(15))

