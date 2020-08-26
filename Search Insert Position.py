class Solution:
    def search_insert_pos(self, nums, target_val):
        """
        Boundary Variables: left = 0, right = len(nums)
        Condition: nums[k] >= target_val
        Return Value: left (after exiting the loop, left is the minimal k satisfying the condition)
        """
        if not nums: return
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target_val:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.search_insert_pos([1, 3, 5, 6], 2))
