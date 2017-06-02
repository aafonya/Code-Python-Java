lenght = 610
section_length = 0.88
width = 268
m = lenght / width

#72, 86, 153, 186, 244


def calc_dist_point(point):
    dist_point = 0.44 + ((point - 1) * 0.88)
    return dist_point


def calc_x_dist_points(y, m):
    x_dist = y / m
    return x_dist

dist_points_y = [calc_dist_point(number) for number in [72, 86, 153, 186, 244]]
dist_points_x = [calc_x_dist_points(number, m) for number in dist_points_y]
