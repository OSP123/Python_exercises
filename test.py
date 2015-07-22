""" Sets the values of the instance variables height and width,
    assuming they are both positive.
"""

"""
	Defines class Rectangle and tests it by creating two Rectangle objects
"""
class Rectangle:
    def __init__ (self):
        self.height = 0
        self.width = 0

    def setData(self, height, width):
        if type(height) != int or type(width)!=int:

            raise TypeError()
        if height > 0 and width < 0:
            self.height = height
        elif height < 0 and width > 0:
            self.width = width
        elif height < 0 and width < 0:
            raise ValueError()
        elif height < 0 or width < 0:
            raise ValueError()

    def __str__(self):
        return "height = %i, and width = %i" % (self.height, self.width)

        
"""
     Creates two Rectangle objects and calls methods on them for testing purposes
"""
if __name__ == "__main__":

    r1 = Rectangle()
    try:
        r1.setData(-3, 4)
    except:
        print ("can't set the Rectangle to a negative value")
    print (r1)
