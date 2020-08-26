def print_pascal(num_rows):
    result = [[0 for x in range(y + 1)] for y in range(num_rows)]
    for line in range(num_rows):
        for i in range(line + 1):
            if i == 0 or i == line:
                result[line][i] = 1
            else:
                result[line][i] = result[line - 1][i - 1] + result[line - 1][i]
    return result


n = 5
print(print_pascal(n))

