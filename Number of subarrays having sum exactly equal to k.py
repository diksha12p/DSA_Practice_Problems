class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # if len(nums) == 1:
        #     if nums[0] == k:
        #         return 1
        #     else:
        #         return 0

        # O(n) solution
        count = 0
        i, j = 0, 1
        s = nums[i:j + 1]
        while j < len(nums):
            if s == k:
                count += 1
                j += 1
            elif s < k:
                j += 1
                s += nums[j]
        else:
            # shrink
            s -= nums[i]
            i += 1

        return count


arr = [10, 2, -2, -20, 10]
arr2 = [9, 4, 20, 3, 10, 5]
arr3 = [1,1,1]
arr4 = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(arr4)):
    for j in range(i+1,len(arr4)):
        print(arr4[i:j])
sol = Solution()
# print(sol.subarraySum(arr3,1))
