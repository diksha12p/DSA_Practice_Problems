class Solution:
    def findMaxLength(self, nums):
        if len(nums)<2:
            return 0

        nums = self._array_update(nums)
        sum_so_far, curr_max_length, dict = 0, 0, {}

        for i in range(len(nums)):
            sum_so_far += nums[i]

            if sum_so_far == 0: curr_max_length = i + 1

            else:
                if sum_so_far not in dict:
                    dict[sum_so_far] = i
                else:
                    curr_max_length = max(curr_max_length, i - dict[sum_so_far])
        return curr_max_length, dict[sum_so_far], dict[sum_so_far] + curr_max_length - 1

    def _array_update(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] =-1
        return nums


sol = Solution()
arr = [0, 0, 1, 1, 0]
print("Length is {} with start index as {} and end index as {}".format(sol.findMaxLength(arr)[0],
                                                                       sol.findMaxLength(arr)[1],
                                                                       sol.findMaxLength(arr)[2]))