from typing import List


def contiguous_array(arr: List[int]) -> int :
    curr_sum, max_length, d = 0, 0, {0: 1}
    for i in range(len(arr)):
        curr_sum += 1 if arr[i] == 1 else -1
        if curr_sum not in d:
            d[curr_sum] = i
        else:
            max_length = max(max_length, i - d[curr_sum])
    return max_length


print(contiguous_array([1,1,0,0,1,1,0,1,1]))