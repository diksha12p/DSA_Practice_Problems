def multiply(num1, num2):
    first = num1 if len(num1) > len(num2) else num2
    second = num2 if len(num1) > len(num2) else num1
    # print(len(first), len(second))
    # i,j = len(first) - 1, len(second) - 1
    result = ""
    carry, prod = 0, 0
    ans = list()
    for j in range(len(second) - 1, -1, -1):
        for i in range(len(first) - 1, -1, -1):
            curr_prod = (int(first[i]) * int(second[j])) + carry
            val = curr_prod % 10
            carry = curr_prod // 10

            result = str(val) + result

        if carry:
            result = str(carry) + result

        prod = int(result) * (10 ** (len(second) - 1 - j))
        # print("{} at {}".format(prod, (10 ** (len(second) - 1 - j))))
        ans.append(prod)

        # val = val + prod
        # print("{} at {}".format(val, (10 ** (len(second) - 1 - j))))


        result , carry= "", 0

    return sum(ans)



n1 = "123"
n2 = "456"
print(multiply(n1,n2))