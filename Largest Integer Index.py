"""
Input a = [21,5,6,56,88,52]
output = [5,5,5,4,-1,-1]

Explanation:
Output array values is made up of indices of the element with value greater than the current element but with
largest index. So 21 < 56 (index 3), 21 < 88 (index 4) but also 21 < 52 (index 5) so we choose index 5 (value 52).
Same applies for 5,6 and for 56 its 88 (index 4). If there is no greater element then use -1 and last element of
the array will always have value of -1 in output array since there is no other element after it.
"""


from typing import List
from collections import OrderedDict


# Basic Approach: Two pointer technique -> O(n^2)
def larger_index(arr: List) -> List:
    result = [-1] * (len(arr))
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] > arr[i]:
                result[i] = j
                break
    return result


# Alternative Approach: Using OrderedDict -> O(n)
def larger_index_d(arr: List) -> List:
    result = [-1] * len(arr)
    val_index_map = OrderedDict()
    val_index_map[arr[-1]] = len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        if higher_key(arr[i], val_index_map):
            result[i] = higher_key(arr[i], val_index_map)
        else:
            val_index_map[arr[i]] = i
    return result


def higher_key(ele, val_index_map):
    for key, value in val_index_map.items():
        if key > ele:
            return value
    return None


def find_right_index(nums):
    from heapq import heappush, heappop
    heap = []
    for i, val in enumerate(nums):
        heappush(heap, (-val, i))
    print(heap)
    res = [-1]*len(nums)
    max_index = -1
    while heap:
        tup = heappop(heap)
        val, curr_index = -tup[0], tup[1]
        if max_index == -1 or curr_index > max_index :
            max_index = max(curr_index, max_index)
            continue
        res[curr_index] = max_index
        max_index = max(curr_index, max_index)
    return res


if __name__ == '__main__':
    print(larger_index([21,5,6,50,88,52, 50]))
    print(larger_index_d([42, 105, 16, 21, 56, 40]))
    print(find_right_index([21,5,6,50,88,52, 50]))
