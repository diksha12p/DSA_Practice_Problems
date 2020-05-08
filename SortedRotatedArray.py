class Solution:
    def _find_pivot(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                return i+1
        return -1

    def _binary_search(self, nums, left, right, target):
        if right < left:
            return -1

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return self._binary_search(nums, mid+1, right, target)
        return self._binary_search(nums, left, mid - 1, target)

    def find_element(self, nums, target):
        pivot = self._find_pivot(nums)
        if pivot == -1:
            self._binary_search(nums, 0, len(nums)-1, target)
        if nums[pivot] == target:
            return pivot
        elif nums[0] <= target:
            return self._binary_search(nums, 0, pivot - 1, target)
        else:
            return self._binary_search(nums, pivot + 1, len(nums) - 1, target)


sol = Solution()
arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
print(sol.find_element(arr1, 3))





