
class Employee3:

    # class variables are variables that are shared among all instances in the class
    # instance variables can be unique for each instance

    # - class variables should be the same for each instance
    # - we can acces class variables easily - emp3_1.raise_amount - accessing through an instance
    # -                                      - Employee3.raise_amount - accessing through the class
    # - we can easily update the value of the class variable
    raise_amount = 1.04

    num_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee3.num_emps += 1
        # in this case, it wouldn't be good if we could change the value of this class variable
        # so we acccess it through the class in this method

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee3.raise_amount)
    # accessing the class variable through class - we can be sure, that the
    # method does always the same thing

    def apply_raise2(self):
        self.pay = int(self.pay * self.raise_amount)
    # using 'self' by accessing the class variable in the method:
    #           - gives us the ability to change the amount for a single instance
    #           - !! it allows any subclass to overwrite that constant (if they want)

    # def apply_raise3(self, var):
        #self.pay = int(self.pay * Employee3.var)


emp3_1 = Employee3('Corey', 'Schafer', 50000)
emp3_2 = Employee3('Test', 'User', 50000)


# about namespaces
#-------------------------------------------------------------------------
# only the class's name space contains the class variable, we can't find it in the instances namespace
# so when we access the class variable through an instance, in the background
# the program is looking for and then finds the class variable in the
# class
print(emp3_1.__dict__)
print(Employee3.__dict__)


# calling our method
#-------------------------------------------------------------------------
# when we call the method on the class, we have to give an instance as an
# argument
Employee3.apply_raise(emp3_1)
print(emp3_1.pay)

# when we call our method on an instance, we do not need the give an argument to the method
#- but in the background happens just the same thing what we did the last time:
# the program is searching for the method in the class which owns the given
# instance
emp3_1.apply_raise()
print(emp3_1.pay)


# changing back the value just because of the next tasks
emp3_1.pay = 50000


# on the difference btw calling the class variable in a method - through classname or - through 'self'
#-------------------------------------------------------------------------
# accessing through classname - when changing the value AND in the method(apply_raise)
# happens just the same for all instances
Employee3.raise_amount = 1.8
Employee3.apply_raise(emp3_1)
Employee3.apply_raise(emp3_2)
print("emp3_1:", emp3_1.pay)
print("emp3_2:", emp3_2.pay)


#!!! but when accessing through an instance by changing the value AND in the method
# the methods doesn't do the same thing
emp3_2.raise_amount = 3
Employee3.apply_raise2(emp3_1)
Employee3.apply_raise2(emp3_2)
print("emp3_1:", emp3_1.pay)
print("emp3_2:", emp3_2.pay)
# when we call the class variable through an instance, the namespace of
# this instance changes, an instance variable is generated here with just
# the same name (we can see it in the namespace of emp3_2 :
print(emp3_1.__dict__)
print(emp3_2.__dict__)
print(Employee3.__dict__)


emp3_1.pay = 50000
emp3_2.pay = 50000

# for the first time it can seem just an odd thing, but this isn't
# it won't cause problem by using our class variable because if we call it through
# the classname in our method, python automatically uses the class
# varibles value by the instance with the modified value (actually with a
# new instance variable) too
Employee3.raise_amount = 0.5
Employee3.apply_raise(emp3_1)
Employee3.apply_raise(emp3_2)
print("emp3_1:", emp3_1.pay)
print("emp3_2:", emp3_2.pay)
