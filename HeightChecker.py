def heightChecker(heights):
    target = sorted(heights)

    output = list(map(lambda x: 1 if x[0] != x[1] else 0, zip(heights, target)))
    return output.count(1)


heights = [1,1,4,2,1,3]
print(heightChecker(heights))


# def commonChars(A):
#     result = list()
#     ref_keys = set(A[0])
#     for ch in ref_keys:
#         times = min([word.count(ch) for word in A])
#         if times:
#             result.extend([ch] * times)
#     return result
#
#
#
#
#
# A = ["bella","label","roller"]
# print(commonChars(A))