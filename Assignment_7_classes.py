""" """
class Employee:
   def __init__(self):
      self.firstName = "Omar"
      self.lastName = "Patel"
      self.sSN = 123456789
      self.salary = 60000.0

   def __str__(self):
      return "%s %s's social security number is %d and salary is %d" % (self.firstName, self.lastName, self.sSN, self.salary)
   def giveRaise(self, percentRaise):
       self.salary += (self.salary * percentRaise)

from employee import Employee

class Manager (Employee):  
   def __init__(self):
        Employee.__init__(self) 
        self.title = "Head Manager"
        self.annualBonus = 5000

   def __str__(self):
        return Employee.__str__(self) + "\nThe title of the manager is %s and the annual bonus is %d" % (self.title, self.annualBonus)    


    

