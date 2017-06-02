class pet:  # this way the class pet is defined

    number_of_legs = 0
    # now the class has a variable - this is changable for every objects in
    # the class


doug = pet()  # this way an object is defined - and this is in the class pet


doug.number_of_legs = 4
# now the variables value is modified -for the instance/object doug


print('Doug has %s legs' % doug.number_of_legs)
