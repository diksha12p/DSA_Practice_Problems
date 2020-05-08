def sort_string(s):
    result = list()
    while len(result) != len(s):
        for i in range(len(set(s))):
            result.append(sorted(set(s))[i])
            print("At {} value is {}".format(i, sorted(set(s))[i]))
        for i in range(len(set(s))):
            result.append(sorted(set(s))[-(1 + i)])
            print("At {} value is {}".format(i, sorted(set(s))[-(1 + i)]))
    return ''.join(ele for ele in result)

str1 = "aaaabbbbcccc"
print(sort_string(str1))