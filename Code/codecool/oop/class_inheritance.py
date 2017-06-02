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

# even without any code of its own, the developer class will have all the
# attributes and methods of our Employee class


class Developer(Employee):
    pass

# instanstiation with the __init__() method of the parent class
# method resolution order - places where python searches for attributes
# and methods
dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'User', 50000)

print(dev_1.pay)
Developer.apply_raise(dev_1)
print(dev_1.pay)

# print(help(Developer))

#-------------------------------------------------------------------------
# making the sublasses own __init__()


class Developer2(Employee):
    raise_amount = 1.10

    # if we want our sublass be able to pass in more attributes than the
    # parent class, we have to write its own __init__() method
    def __init__(self, first, last, pay, prog_lang):
        # we can write this method in two different way
        # in order to let the parent classes __init__() method to  handle the first x attributes
        # than the subclasses  __init__() method will handle only its own attributes
        # using super()

        # using super is important by multiple inheritance
        super().__init__(first, last, pay)
        # another way to do this logic above
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

dev2_1 = Developer2('Corey', 'Schafer', 50000, 'Python')
dev2_2 = Developer2('Test', 'User', 50000, 'Java')

print(dev2_1.pay)
Developer2.apply_raise(dev2_1)
print(dev2_1.pay)

print(dev2_2.prog_lang)

#--------------------------------------------------------------------------
# making another subclass  - takes in a list as an argument


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, new_emp):
        if new_emp not in self.employees:
            self.employees.append(new_emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname())

mng_1 = Manager('Sue', 'Smith', 90000, [dev2_1])

print(mng_1.email)
print(mng_1.employees)

print("mng_1 - employees before calling any methods")
mng_1.print_employees()


mng_1.add_emp(dev2_2)
print("mng_1 - employees after calling adding method")
Manager.print_employees(mng_1)


mng_1.remove_emp(dev2_1)
print("mng_1 - employees after calling removing method")
Manager.print_employees(mng_1)

# isinstance and issubclass built-in functions
print(isinstance(mng_1, Manager))
print(issubclass(Manager, Employee))
