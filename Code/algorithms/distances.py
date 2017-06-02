begin_y = 25.8
end_y = 6

begin_x = 14.1
end_x = 22.8


def convert_coord(degree, convert):
    #converted = degree + ((convert * 16.67) / 1000)
    converted = (convert * 16.67) / 1000
    return converted

converted_begin_y = convert_coord(17, begin_y)
converted_end_y = convert_coord(17, end_y)

converted_begin_x = convert_coord(47, begin_x)
converted_end_x = convert_coord(47, end_x)

length = converted_begin_y - converted_end_y
width = converted_end_x - converted_begin_x


def distance_convert(length):
    converted = length * 1.85
    return converted

converted_length = distance_convert(length)
section_length = converted_length / 694
converted_width = distance_convert(width)

print("x1 y1 {} {}" .format(converted_begin_x, converted_begin_y))
print("x2 y2 {} {}" .format(converted_end_x, converted_end_y))
print(converted_begin_y)
print(converted_end_y)
print(length)
print(width)
print(converted_length)
print(section_length)
print(converted_width)
