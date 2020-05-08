def oddCells(n, m, indices):
    M = [[0 for j in range(m)] for i in range(n)]
    for index in indices:
        row, col = index[0], index[1]
        for k in range(m):
            M[row][k] += 1
        for k in range(n):
            M[k][col] += 1
    # print(M)

    count = 0
    for index_row in range(n):
        for index_col in range(m):
            if M[index_row][index_col] % 2 != 0:
                count += 1
    return count


n = 2
m = 3
indices = [[0,1],[1,1]]
print(oddCells(n,m,indices))