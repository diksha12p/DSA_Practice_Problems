def getKth(lo: int, hi: int, k: int) -> int:
    # numbers = [ele for ele in range(lo, hi + 1)]

    if lo == hi:
        return lo

    result = list()
    for ele in range(lo, hi + 1):
        result.append([ele, power(ele)])

    result.sort(key=lambda x: x[1])

    return result[k-1][0]


def power(ele):
    prev_results = {1: 1}
    if ele not in prev_results:
        if ele % 2:
            prev_results[ele] = 1 + power(3 * ele + 1)
        else:
            prev_results[ele] = 1 + power(ele / 2)
    return prev_results[ele]
    # count = 0
    # while ele != 1:
    #     if ele % 2:
    #         ele = 3 * ele + 1
    #         count += 1
    #     else:
    #         ele = ele / 2
    #         count += 1
    # return count


lo, hi, k = 1, 1000, 777
# print(power(3))
print(getKth(lo,hi,k))
