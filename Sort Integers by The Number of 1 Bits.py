# arr = [0,1,2,3,4,5,6,7,8]
# bin_arr = list(map(lambda x: bin(x)[2:].count('1'), arr))
# zip = list(zip(arr,bin_arr))
# sorted_zip = sorted(zip, key = lambda x: (x[1], x[0]))

# print([x[0] for x in sorted_zip])

S = "a1b2"
ans = list()
for s in S:
    if s.isdigit():
        continue
    else:
        ans.append(s)
print(2*len(ans))