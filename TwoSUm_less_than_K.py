"""
LC 1099. Two Sum Less Than K (https://leetcode.com/problems/two-sum-less-than-k/): Given an array A of integers and integer K,
return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.


Examples:

Input : arr = {30, 20, 50} , K = 70
Output : 30, 20
30 + 20 = 50 which is maximum possible usm which is less than K


Input : arr = {5, 20, 110, 100, 10}, K = 85
Output : 20, 10

"""


def sum_less_than_k(nums : list, k : int) -> tuple:
    nums.sort()
    curr_max = 0
    p, x, y = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] >= k:
            p = i
            break

    for i in range(p):
        for j in range(i+1,p):
            if curr_max < nums[i] + nums[j] < k:
                curr_max = nums[i] + nums[j]
                x, y = nums[i], nums[j]

    return x, y




