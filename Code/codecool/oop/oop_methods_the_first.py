class pet:  # this way the class pet is defined

    number_of_legs = 0
    # now the class has a variable - this is changable for every objects in
    # the class

    def sleep(self):
        print("zzz")

    def count_legs(self):
        print('Doug has %s legs.' % doug.number_of_legs)
    # this method works good for one and only one instance - because its
    # name is what stands before the name of the variable

    def count_legs_universally(self):
        print('Doug has %s legs.' % self.number_of_legs)
    # this way the method works for any instance in the class

doug = pet()  # this way an object is defined - and this is in the class pet
doug.number_of_legs = 4

nemo = pet()
nemo.number_of_legs = 0

doug.sleep()
doug.count_legs()

nemo.count_legs_universally()
