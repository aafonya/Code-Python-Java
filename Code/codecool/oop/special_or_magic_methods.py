# these special methods allows us to emulate some built-in behaviour within python
#
# by defining our own special methods we'll be able to change some of
# these built-in behaviours and operations

# surrounded by double underscores - dunder
# e.g. __init__ is the most common special method


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

 # __repr__() and __str__() - for debugging - we can defining the
 # representation of an object
    def __repr__(self):
        return "Employee ({} {} {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 50000)


print(emp_1)

print(repr(emp_1), ' ', "with repr()")
print(str(emp_1), ' ', "with str()")
# these lines directly calls the next special methods:
print(emp_1.__repr__(), ' ', "with __repr__()")
print(emp_1.__str__(), ' ', "with __str__()")


# if I write this:
# ~ print(1+2)
# the python code actually calls this method:
print(int.__add__(1, 2))

# if I write this:
# ~ print("a" + "b")
# the python code actually calls this method:
print(str.__add__("a", "b"))

# here I call my own classes magic method __add__()
# it sums the payments of the employees - just because I said that:) but,
# I can actually write anything
print(emp_1 + emp_2)

# this just also use a special method in the background
print(len('test'))
print('test'.__len__())

# calling my own __len__():
print(len(emp_1))
