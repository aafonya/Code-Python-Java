#-*- encoding: utf - 8 - *-

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory():  # prints the inventory
    print("Inventory")
    a = 0
    for i in inv:
        print(i + " " + str(inv[i]))
        a = a + inv[i]
    print("Total number of items:" + str(a))


def add_to_inventory(inv, dragon_loot):  # merges the inventory and a list
    for i in dragon_loot:
        if i in inv:
            inv[i] += 1
        if i not in inv:
            inv[i] = 1
    return inv


def print_table(order):
    order = input(
        "Do you want to see your list unordered ( press Enter), in ascending order(asc) or in descending order(desc)? ")
    print("Inventory")

    width_of_keys = []
    width_of_values = []
    longest_keys = 0
    longest_values = 0

    # making a list to store the longevity of the keys and values
    for i in inv:
            width_of_keys.append(len(i))
            width_of_values.append(len(str(inv[i])))
            # to store the number of the characters of the longest keys and
            # values
            longest_keys = max(width_of_keys)
            longest_values = max(width_of_values)

    print ((" " * longest_values) + "count" +  # printing the first of the table - with paying attention to the width of the column
           (" " * longest_keys) + "item name")
    # printing a line - as long as the widht of the whole table
    print(("-") * (longest_keys + longest_values + 5 + 9))

    a = 0

    if order == "":  # prints the inventory unordered
        for i in inv:
            print(" " * (longest_values + 5 -
                         len(str(inv[i]))) + str(inv[i]) + " " * (longest_keys + 9 - len(str(i))) + i)
            a = a + inv[i]

    if order == "asc":  # prints the inventory in ascending order
        for i in sorted(inv, key=inv.get, reverse=False):
            print(" " * (longest_values + 5 -
                         len(str(inv[i]))) + str(inv[i]) + " " * (longest_keys + 9 - len(str(i))) + i)
            a = a + inv[i]

    if order == "desc":  # prints the inventory in descending order
        for i in sorted(inv, key=inv.get, reverse=True):
            print(" " * (longest_values + 5 -
                         len(str(inv[i]))) + str(inv[i]) + " " * (longest_keys + 9 - len(str(i))) + i)
            a = a + inv[i]

    # printing a line - as long as the widht of the whole table
    print(("-") * (longest_keys + longest_values + 5 + 9))
    print("Total number of items: " + str(a))


def import_inventory(filename="import_inventory.csv"):
    imported_keysandvalues = {}
    myimport = open(filename, "r")
    for i in myimport:
        myrows = i.split(",")  # splits the imported rows by the columns
        # the head of the table won't be imported to the dictionary - because
        # of the enter following 'count''
        if myrows[1] != "count\n":
                # stores the splitted rows (keys and values) in a dictionary
                imported_keysandvalues[myrows[0]] = int(myrows[1])
    for i in imported_keysandvalues:  # merges the inventory and the dictionary with the imported keys and values
        if i in inv:
            inv[i] += imported_keysandvalues[i]
        if i not in inv:
            inv[i] = imported_keysandvalues[i]
    return inv


def export_inventory(filename="export_inventory.csv"):
    myfile = open(filename, "w")
    myfile.write(str(inv))

order = ""
display_inventory()
inv = add_to_inventory(inv, dragon_loot)
display_inventory()

print_table(order)

import_inventory()
display_inventory()

export_inventory()
