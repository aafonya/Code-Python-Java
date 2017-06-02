# differences between
#                   regular methods
#                   class methods
#                   static methods

# regular methods:
#               automatically takes the instance as the first argument (by convention we call it 'self')
# class methods:
#               automatically takes the class as the first argument (by convention we write 'cls')
#               decorator: @classmethod

#               they can be used as "alternative constructor"
# static method:
#              decorator: @staticmethod


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 50000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# we can run class methods from the class
Employee.set_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# we can run class methods from instances too
emp_1.set_amount(1.08)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
