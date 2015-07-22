"""
Employee File defines Employee Class.
"""
from functools import total_ordering

@total_ordering
class Employee:
   """
   An object of this class stores a first name, last name, social security
   number, and salary, which can be set by sending it to the object params. The
   class does have equality and comparison operator methods, a constructor method,
   an output string method, and a method that allows the user to give a raise
   to employee objects.
   """
   def __init__(self, firstName, lastName, sSN, salary):
      """
      Sets firstName, lastName, ssn, and salary and checks for bad data. Uses
      default values if arguments are invalid.
      """
      if type(firstName) == str and type(lastName) == str:
         self.firstName = firstName
         self.lastName = lastName
      else:
         self.firstName = "Jack"
         self.lastName = "Sparrow"
      if type(sSN) == int and sSN > 0 and sSN < 1000000000:
         self.sSN = sSN
      else:
         self.sSN = 123456789
      if type(salary) == float or type(salary) == int:
         self.salary = salary
      else:
         self.salary = 60000.0

   def __eq__(self,other):
      """
      Checks if firstName and lastName of two objects are equal.
      """
      return self.firstName == self.lastName and other.firstName == self.lastName

   def __lt__(self,other):
      """
      Checks if lastName of first object is less than second's. If last names are
      equal, it checks if firstName of first object is less than second's.
      """
      if self.lastName.lower() < other.lastName.lower():
         return True
      elif self.lastName.lower() > other.lastName.lower():
         return False
      else:  # last names are equal
         return self.firstName.lower() < other.firstName.lower()
         
   def __str__(self):
      """
      Returns a string output of object
      """
      return "%s %s's social security number is %d and salary is %d" % (self.firstName, self.lastName, self.sSN, self.salary)

   def giveRaise(self, percentRaise):
      """
      Raises the salary of an Employee instance by the number sent in as argument
      """
      self.salary += (self.salary * percentRaise)


    

