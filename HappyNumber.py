def isHappy(n):
    result = check(n)
    for i in range(10):
        if result == 1:
            print("Happy Number !!")
            break
        else:
            # print("In else loop")
            result = check(result)


def check(number):
    # result = 0
    list_nums = list(map(int, str(number)))
    number = sum(map(lambda x: x * x, list_nums))
    # print(number)
    return number


def alt_isHappy(n):
    sum_squares_list = list()
    n = check(n)
    while n not in sum_squares_list:
        sum_squares_list.append(n)
        if n == 1:
            print("Happy Number !!")
            break
        else:
            n = check(n)


# print(check(19))
alt_isHappy(19)


