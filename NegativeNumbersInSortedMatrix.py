def count_negatives(grid):
    count = 0
    for list_nums in grid:
        for index in range(len(list_nums)):
            if list_nums[index] >= 0:
                continue
            else:
                count += int(len(list_nums) - index)
                break
    return count


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(count_negatives(grid))