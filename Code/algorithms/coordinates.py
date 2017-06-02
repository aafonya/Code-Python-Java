#              y1     x1    y2   x2
coordinates = (25.8, 14.1, 6.0, 22.8)
converted_coordinates = []
points_on_line = [72, 86, 153, 186, 244]
point_coord = {}


def convert_coord(convert):
    converted = (convert * 16.67) / 1000
    return converted


for coordinate in coordinates:
    converted_coordinates.append(convert_coord(coordinate))

for coord in converted_coordinates:
    print(coord)

length = converted_coordinates[0] - converted_coordinates[2]
width = converted_coordinates[3] - converted_coordinates[1]
m = length / width
section_length = length / 694


def calc_y(point):
    point_y = (section_length / 2) + ((point - 1) * section_length)
    return point_y


def calc_x_dist_points(y, m):
    point_x = y / m
    return point_x

for point in points_on_line:
    y = calc_y(point)
    point_coord[point] = [calc_y(point)]
    point_coord[point].append(calc_x_dist_points(y, m))

for key in point_coord:
    print(point_coord[key])
