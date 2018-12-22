"""

"""

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

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


    # How does the class variable apply to the self tag here.

    # repr and str are the most fundamental dunder objects
    # repr is unambigious representation of object. For developers, for debugging
    # str is a readable interpretation and used for user views


emp1 = Employee('Henry','Gilbert',70000)

# Both these commands return the same value.

"""
print(str(emp1))
print(emp1.__str__())

print(repr(emp1))
print(emp1.__repr__())

emp2 = Employee('James',"White",54000)
print(emp1+emp2)
"""

# These emulate build in arithmetic functions. Useful for methods that are
# special to whatever operations you need.
print(len(emp1))
