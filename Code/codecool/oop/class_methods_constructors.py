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

    # using the classmethod as an alternative constructor
    #-------------------------------------------------------------------------
    # making new objects from strings
    @classmethod
    def from_new_str(cls, emp_str):
        first, last, pay = emp_str.split('_')
        return cls(first, last, pay)


str_1 = 'John_Doe_50000'
str_2 = 'Joe_Dante_60000'
str_3 = 'Jodie_Davy_70000'

new_emp_1 = Employee.from_new_str(str_1)
new_emp_2 = Employee.from_new_str(str_2)
new_emp_3 = Employee.from_new_str(str_3)

print(new_emp_3.pay)
