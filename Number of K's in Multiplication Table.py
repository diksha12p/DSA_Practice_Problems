"""
Daily Coding Problem # 74
This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th
column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N
multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

1	2	3	4	5	6
2	4	6	8	10	12
3	6	9	12	15	18
4	8	12	16	20	24
5	10	15	20	25	30
6	12	18	24	30	36

And there are 4 12's in the table.
"""


def get_mult_count(n, x):
    if n == 1:
        return n

    # count = 0
    # for i in range(1, n):
    #     if not x % i:
    #         count += 1
    # return count

    return sum(1 for i in range(1, n) if x % i == 0)


def get_mult_count_naive(n, x):
    count = 0
    for i in range(n):
        for j in range(n):
            if (i + 1) * (j + 1) == x:
                count += 1
    return count


assert get_mult_count(1, 1) == 1 == get_mult_count_naive(1, 1)
assert get_mult_count(6, 12) == 4 == get_mult_count_naive(6, 12)
assert get_mult_count(2, 4) == 1 == get_mult_count_naive(2, 4)
assert get_mult_count(3, 6) == 2 == get_mult_count_naive(3, 6)



