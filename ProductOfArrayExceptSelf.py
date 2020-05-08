from functools import reduce


class Solution:
    def productExceptSelf(self, nums):
        product_list = list()
        result_arr = [nums[:i] + nums[i+1:] for i in range(len(nums))]
        for item in result_arr:
            product_list.append(reduce(lambda x,y: x*y, item))
        return product_list


nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))




