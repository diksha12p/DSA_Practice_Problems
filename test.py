m, n = 5, 7
# nums = list(range(m,n+1))
# print(nums)
# result = nums[0] & nums[1]
# for i in range(2, len(nums) - 1):
#     print(nums[i],nums[i+1])
#     result = int(nums[i]) & int(nums[i+1]) & result
#     # print(nums[i])


# nums = list(range(m,n+1))
# for i in range(0,len(nums) - 1, 1):
#     # print(i)
#     if i == 0:
#         nums[0] = nums[0] & nums[1]
#     else:
#         nums[0] = nums[i] & nums[i+1] & nums[0]
# print(nums[0])


while(m < n):
    n -= (n & -n)
print(n)

m, n = 5, 7
print(5&6&7)
nums = [bin(num) for num in range(m,n+1)]
print(nums)
count_arr = [ele.count("1") for ele in nums]
print(count_arr)
print(min(count_arr))
