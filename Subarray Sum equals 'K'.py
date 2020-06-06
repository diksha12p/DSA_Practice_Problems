from typing import List


def subarray_K(arr : List[int], K : int) -> int:
    curr_sum, count, d = 0, 0, {0:1}
    for i in range(len(arr)):
        curr_sum += arr[i]
        if (curr_sum - K) in d.keys():
            count += d[curr_sum - K]

        if curr_sum not in d:
            d[curr_sum] = 1
        else:
            d[curr_sum] += 1
    return count


print(subarray_K([0,0,0,0,0,0,0,0], 0))