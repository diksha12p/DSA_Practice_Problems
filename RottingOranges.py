def orangesRotting(grid) -> int:
    if not len(grid) or not len(grid[0]):
        return -1
    fringe, count = [], -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                fringe.append((i, j))

    while fringe:
        for i in range(len(fringe)):
            curr_row, curr_col = fringe.pop(0)

            for x, y in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1),
                         (curr_row, curr_col + 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = 2
                    fringe.append((x, y))

        count += 1

    flag = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                flag = True

    if not flag:
        return count
    else:
        return -1


matrix = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(matrix))