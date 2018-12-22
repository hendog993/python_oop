class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)
    # you can override the top method in init to make this work, but not efficient.

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    # Calculate total salaries for all employees
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp1 = Employee('John','Smith',60000)

# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())

# Notice how the email is not updated properly. Similar to getter and setter methods in Java.
# Could create an email method separately. But, this breaks the code.
# Property decorator allows us to define method and access like an attribute

# Here we want this to change our whole configuration. This only changes
# the whole fullname. Can't set individual attributes with this style.
# Will not update the actual first name, last name, or email.

# Usefulness of setters. Compare the two codes.

emp2 = Employee('James','Harrison',45948)
emp2.fullname = 'Henry Gilbert'
print(emp2.first)
print(emp2.email)
print(emp2.fullname)

# Without a setter here, trying to change the fullname will
# result in an error. This is because it can not change the
# variables without a setter method. Using just a property
# decorator, it tries to



