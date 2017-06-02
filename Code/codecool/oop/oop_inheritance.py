class pet:  # this way the class pet is defined

    number_of_legs = 0
    # now the class has a variable - this is changable for every objects in
    # the class

    def sleep(self):
        print("zzz")

    def count_legs_universally(self):
        print('Doug has %s legs.' % self.number_of_legs)
    # this method works good for any instances


class dog(pet):
    # this is a subclass, it is in the pet class and inherits all of its
    # methods, variables etc.

    number_of_legs = 4

    def bark(self):
        print("woof")

doug = dog()
doug.bark()
doug.sleep()
doug.count_legs_universally()
