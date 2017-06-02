class Complex:

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def full_number(self):
        return '{}{}'.format(self.r, self.i)

x = Complex(3.0, -4.5)
print(x.r, x.i)

print(x.full_number())


class Employee3:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp3_1 = Employee3('Corey', 'Schafer', 50000)
emp3_2 = Employee3('Test', 'User', 50000)

emp3_1.raise_amount = 1.5
print(emp3_1.__dict__, emp3_2.__dict__)
print(emp3_2.__dict__, emp3_2.__dict__)
print(Employee3.__dict__, emp3_2.__dict__)

Employee3.apply_raise(emp3_1)
Employee3.apply_raise(emp3_2)
print(emp3_1.pay, emp3_2.pay)

Employee3.raise_amount = 2
print(emp3_1.__dict__, emp3_2.__dict__)
print(emp3_2.__dict__, emp3_2.__dict__)
print(Employee3.__dict__, emp3_2.__dict__)

Employee3.apply_raise(emp3_1)
Employee3.apply_raise(emp3_2)
print(emp3_1.pay, emp3_2.pay)
