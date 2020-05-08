class Solution:
    def minSubsequence(self, arr):
        sum1, sum2 = 0, sum(arr)
        arr.sort()
        for i in range(len(arr) - 1, -1, -1):
            sum1 += arr[i]
            sum2 -= arr[i]
            if sum1 > sum2: return sorted(arr[i:], reverse=True)


sol = Solution()
nums = [6]
print(sol.minSubsequence(nums))