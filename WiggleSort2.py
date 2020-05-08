class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        odd_index = sorted(nums)[len(nums) // 2:]
        even_index = sorted(nums)[:len(nums) // 2]


        if len(nums) % 2 == 1:  # hanle odd cases
            even_index.append(odd_index[0])
            odd_index.pop(0)

        nums[1::2] = odd_index[::-1]
        nums[::2] = even_index[::-1]
        print(nums)


arr = [4,5,5,6]
sol = Solution()
sol.wiggleSort(arr)