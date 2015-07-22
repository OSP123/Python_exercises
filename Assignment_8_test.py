"""
Test File. Created employee/manager objects and stored them into list. Then,
manually tested __lt__ on two sets of objects. Finally, did a sort() call
on the employeeList and then checked to see if the sort used __lt__. Also,
confirmed new method, __lt__ is consistent by having two employee objects with
same last name but different first names in list. 
"""
from employee import Employee
from manager import Manager

#testing
employee1 = Employee("Mexico", "Ferrari", "123Hey", 1234123)
employee2 = Employee("Max", "Power", 123098222, "meow")
employee3 = Employee("Gertrude", "Rowenthall", 123098222, "meow")
employee4 = Employee("Steve", "Yunder", 123098222, "meow")
employee5 = Employee("Bill", "Yunder", 123098222, "meow")
manager1 = Manager("Mega Manager", 7000)
manager2 = Manager("Meh Manager", 2000)

employeeList = [employee1, employee2, employee3, employee4, employee5, manager1, manager2]

for employee in employeeList:
    print(employee.lastName + " " + employee.firstName)

print("\n")

print(employee1 < employee2)
print(employee2 > manager2)

print("\n")

employeeList.sort();

for employee in employeeList:
    print(employee.lastName + " " + employee.firstName)

"""------------------------------------Output-----------------------------------
Ferrari Mexico
Power Max
Rowenthall Gertrude
Yunder Steve
Yunder Bill
Generic Last Name Generic First Name
Generic Last Name Generic First Name


True
True


Ferrari Mexico
Generic Last Name Generic First Name
Generic Last Name Generic First Name
Power Max
Rowenthall Gertrude
Yunder Bill
Yunder Steve
-----------------------------------------------------------------------------"""
