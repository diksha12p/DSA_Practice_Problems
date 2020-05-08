
def smaller_numbers_than_current(nums):
    result = list()
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
    return result


def count_smaller_numbers(nums):
    dict_result = {}
    sorted_nums = sorted(nums)
    result = []
    for ele in sorted_nums:
        if ele not in dict_result:
            dict_result[ele] = sorted_nums.index(ele)
    for elem in nums:
        result.append(dict_result[elem])
    return result


def method_alt(nums):
    result = []
    temp_nums = nums.copy()
    nums.sort()
    for n in temp_nums:
        result.append(nums.index(n))
    return result


nums = [8,1,2,2,3,2,8]
print(smaller_numbers_than_current(nums))
print(count_smaller_numbers(nums))
print(method_alt(nums))



