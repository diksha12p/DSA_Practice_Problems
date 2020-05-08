def findMin(nums) -> int:
    if not nums:
        return 
    if len(nums) == 1:
        return nums[0]
    else:
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                return nums[i + 1]
        return nums[0]


arr = [3,4,5,1,2]
print(findMin(arr))