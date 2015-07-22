
from employee import Employee

"""
An object of this class represents a manager with the attributes inherited
from Employee and the additional data members: title and annual bonus.
"""
class Manager (Employee):
    
   """
   An object of this class stores a title and annual bonues of a manager, along with
   the attributes from employee. The only methods exclusive to manager include
   a string output method and a constructor.
   """
   def __init__(self, title, annualBonus):
        """
        Sets the employee default values, title, and annual bonus. It also
        checks to see if values are valid and sets them to default values if they
        aren't.
        """
        Employee.__init__(self, "Generic First Name", "Generic Last Name", 123456789, 60000)
        if type(title) == str:
            self.title = title
        else:
            self.title = "Head Manager"
        if type(annualBonus) == int or type(annualBonus) == float:
            self.annualBonus = annualBonus
        else:
            self.annualBonus = 5000.0
    
   def __str__(self):
      """
      String output method with Employee object string method combined with Manager data.
      """
      return Employee.__str__(self) + "\nThe title of the manager is %s and the annual bonus is %d" % (self.title, self.annualBonus)    
