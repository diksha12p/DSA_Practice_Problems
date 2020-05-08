def maximum69Number(num):
    digits_list = extract_digits(num)
    for index in range(len(digits_list)):
        if digits_list[index] == 6:
            digits_list[index] = 9
            break
    return "".join(str(digit) for digit in digits_list)


def extract_digits(num):
    extracted_digits = list()
    while num > 0:
        extracted_digits.append(num % 10)
        num = num // 10
    return extracted_digits[::-1]


num = 669
print(maximum69Number(num))

