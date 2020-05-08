def kmp_algo(haystack, needle):
    # # Constructing the temp array
    temp = [0] * len(needle)
    i,j = 1,0
    while i < len(needle):
        if needle[i] == needle[j]:
            temp[i] = j + 1
            i += 1
            j += 1

        else:
            if j == 0:
                j = 0
            else:
                j = temp[j-1]
            if needle[i] != needle[j]:
                temp[i] = 0
                i += 1

    h,n = 0,0
    while h < len(haystack) and n<len(needle):
        if haystack[h] == needle[n]:
            h+= 1
            n+= 1
        else:
            if n == 0:
                h += 1
            else:
                n = temp[n-1]

    if n == len(needle):
        return h - len(needle)
    else:
        return -1


txt = "AAAAABAAABA"
pat = "AAAA"
print(kmp_algo(txt, pat))


