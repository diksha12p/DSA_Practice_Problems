def reverse(num):
    if num > 0:
        return "".join(str(ele) for ele in list(str(num))[::-1])
    elif num < 0:
        return "".join(str(ele) for ele in ["-"] + list(str(abs(num)))[::-1])
    else:
        return 0



num = -122
print(reverse(num))