def print_menu(first_str, sec_str):

    tag_clouds = ["1", "2", "3", "4"]
    width_of_table = 0
    if first_str > sec_str:
        width_of_table = len(first_str) + 22
    else:
        width_of_table = len(sec_str) + 22

    for i in range(0, 17):
        if i in (0, 1, 3, 6, 12, 13, 16, 17):
            print("_" * (width_of_table - 2))
        if i == 2:
            print((" " * round(((width_of_table - 2 - len(first_str)) / 2))) +
                  first_str +
                  (" " * round(((width_of_table - 2 - len(first_str)) / 2)))
                  )
        if i == 5:
            print((" " * round(((width_of_table - 2 - len(sec_str)) / 2))) +
                  sec_str + (" " * round(((width_of_table - 2 - len(sec_str)) / 2))))
        if i == 8:
            for i in tag_clouds:
                print((" " * round(((width_of_table - 3) / 2))) +
                      i + (" " * round(((width_of_table - 3) / 2))))
        if i == 15:
            print((" " * round(((width_of_table - 6) / 2))) +
                  "Exit" + (" " * round(((width_of_table - 6) / 2))))

print_menu('Menu', 'Tag clouds')
