#  Create a class called employees and create a method to provide full name of an employee

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    

emp_1 = Employee("Nilesh", "Chaudhari", 3000)
emp_2 = Employee("Chirag", "Gaikwad", 3500)

emp_1.fullname()
