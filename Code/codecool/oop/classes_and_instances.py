class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

# instance variables: contain data that are unique to each instance
# creating instance variable - manually
emp1.first = "Corey"
emp1.last = "Schafer"
emp1.email = "corey.shafer@gmail.com"
emp1.pay = 50000

emp2.first = "Test"
emp2.last = "Uer"
emp2.email = "test.user@gmail.com"
emp2.pay = 60000

# accessing these instance variables
print(emp1.email)
print(emp2.email)


#-------------------------------------------------------------------------
# and now we're gonna setting up the instance variable automatically - for
# the next class
#- by using the __init__ method

class Employee2:

    # after self we can specify which other arguments we want to accept
    # ! the email attribute is gonna be created by using 'first' and 'last'
    def __init__(self, first, last, pay):
        self.first = first  # it is the same thing as doing this: emp1.first = "Corey" but certainly it works universally and automatically for all of instances
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

# so now instansctiation is much more shorter
# the __init__method will be run automatically
# - emp2_1 will be passed in as 'self'
# - and it will set to all of the attributes
emp2_1 = Employee2('Corey', 'Schafer', 50000)
emp2_2 = Employee2('Test', 'User', 60000)

print(emp2_1.email)
print(emp2_2.email)

#-------------------------------------------------------------------------
# to perform some kind of action - we are gonna doing methods
# e.g. to display the full name of an employee


class Employee3:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

emp3_1 = Employee3('Corey', 'Schafer', 50000)
emp3_2 = Employee3('Test', 'User', 60000)


print(emp3_1.full_name())

# calling the instance method on the class
print(Employee3.full_name(emp3_1))
