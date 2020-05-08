class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)

    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        positive = self.dp(nums, target, index - 1, curr_sum + nums[index])
        negative = self.dp(nums, target, index - 1, curr_sum + -nums[index])

        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]


        # def _rec(p, curr_sum):
        #     if p < 0 and curr_sum == S:
        #         return 1
        #     elif p < 0:
        #         return 0
        #     else:
        #         return _rec(p-1, curr_sum + nums[p]) + _rec(p-1, curr_sum - nums[p])
        #
        # return _rec(len(nums) - 1, 0)


arr = [-3, 1, 3, 5, 7]
arr2 = [-3, 1, 3, 5]

# target number
k = 6
sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1],3))