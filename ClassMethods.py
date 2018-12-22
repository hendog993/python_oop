# learn the difference between regular, class, and static method
# Regular methods automatically take the instance as the first arg

# How to take class as the first argument
# To turn a regular method into class method, add @classmethod

# A class method takes the class as the first argument instead of instance
# Regular methods take


"""
============class method syntax==============
@classmethod
def from_functionName(cls, arguments):
    return cls(arguemnts) <-- inputs the arguemnts into the initial class

    to call the class method, use
    Classname.classmethodname(arguemtns)

"""

class Employee():

    raise_amount = 1.05  # written as a percentage
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def raise_salary(self, newSalary):
        self.salary = newSalary
        return
        
    @classmethod
    def hyphen_constructor(cls, empstr):
        name, salary, pay = empstr.split("-")
        return cls(name,salary,pay)

    @staticmethod
    def check_integ_department(self):
        if self.department == "Integration":
            print("True")
            return True
        else:
            print("False")
            return False
    @staticmethod
    def check_salary(self):
        if self.department == "Engineering" and self.salary < 60000:
            print("You are being low-balled")
        else:
            print("Acceptable salary")
        return

    pass

## Class methods can be used as an alternative constructor
# Classic constructor here
emp1 = Employee("Henry Gilbert", 50000, "Engineering")
print(emp1.name)
print(emp1.salary)
print(emp1.department)

# Alternative constructor using class methods
raid = "Derrick Sherrill-65000-Rotational"
emp2 = Employee.hyphen_constructor(raid)
print(emp2.name)
print(emp2.salary)
print(emp2.department)

# Static methods. What is the main difference btn static and class??
# class pass class, regular methods pass instance, static pass nothing auto
# behave like regular classes but have a logical connection to the class

v = Employee.check_integ_department(emp2)
check1 = Employee.check_salary(emp1)

# Static methods can check instances or classes. Just depends on what you want
