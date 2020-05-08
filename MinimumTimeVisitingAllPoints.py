def min_time_to_visit_all_points(points):
    count = 0
    for index in range(len(points)-1):
        start_point, end_point = points[index], points[index + 1]
        count += max(abs(end_point[0] - start_point[0]), abs(end_point[1] - start_point[1]))
    return count


points = [[1,1],[3,4],[-1,0]]
print(min_time_to_visit_all_points(points))
