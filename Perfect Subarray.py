from typing import List


def perfect_subarray(arr: List[int]) -> int:
    curr_sum, min_sum, count, d = 0, 0, 0, {0 : 1}
    for i in range(len(arr)):
        curr_sum += arr[i]
        min_sum, j = min(min_sum, curr_sum), 0
        while (curr_sum - j*j) >= min_sum:
            if (curr_sum - j*j) in d.keys():
                count += d[curr_sum - j*j]
            j += 1
        if curr_sum in d.keys():
            d[curr_sum] += 1
        else:
            d[curr_sum] = 1
    return count


array = [-5, -1, 1, 9]
print(perfect_subarray(array))




