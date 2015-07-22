"""
Test File. Testing all 3 phases of the program in different parts. I've also
imported each file and the relevant classes. 
"""

from employee import Employee
from manager import Manager

#Phase I testing
employee = Employee("Banana", "Thompson", 645348788, 1234123)
print (employee)
employee.giveRaise(0.1)
print (employee)

#Phase II testing
manager = Manager("Super Manager", 4500)
manager.giveRaise(0.3)
print(manager)
print("\n")

#Phase III testing
employee1 = Employee("Mexico", "Ferrari", "123Hey", 1234123)
employee2 = Employee("Max", "Power", 123098222, "meow")
manager1 = Manager("Mega Manager", 7000)
manager2 = Manager("Meh Manager", 2000)

employeeList = [employee1, employee2, manager1, manager2]

for employee in employeeList:
    print(employee)

print("\n")

for employee in employeeList:
    employee.giveRaise(0.1)
    print(employee)

"""------------------------------------Output-----------------------------------
Banana Thompson's social security number is 645348788 and salary is 1234123
Banana Thompson's social security number is 645348788 and salary is 1357535
Generic First Name Generic Last Name's social security number is 123456789 and salary is 78000
The title of the manager is Super Manager and the annual bonus is 4500
Mexico Ferrari's social security number is 123456789 and salary is 1357535
Max Power's social security number is 123098222 and salary is 66000
Generic First Name Generic Last Name's social security number is 123456789 and salary is 66000
The title of the manager is Mega Manager and the annual bonus is 7000
Generic First Name Generic Last Name's social security number is 123456789 and salary is 66000
The title of the manager is Meh Manager and the annual bonus is 2000
-----------------------------------------------------------------------------"""
