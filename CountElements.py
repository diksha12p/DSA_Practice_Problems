from collections import Counter


def countElements(arr):
    count = 0
    d = Counter(arr)
    for key in sorted(d.keys()):
        if key + 1 in d:
            if d[key] == d[key + 1]:
                count += d[key]
            elif d[key] > d[key + 1]:
                count += d[key]
            else:
                count += min(d[key], d[key + 1])
    return count


arr = [1,3,2,3,5,0]
print(countElements((arr)))