"""
	Defines class Rectangle and tests it by creating two Rectangle objects
"""
class Rectangle:
    def __init__ (self):
        self.height = 0
        self.width = 0

    def setData(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return "height = %i, and width = %i" % (self.height, self.width)

    def area(self):
        theArea = self.height * self.width
        return theArea

if __name__ == "__main__":
    r1 = Rectangle()
    print (r1)   # automatcially calls __str__(self) method and prints the returned value
    r1.setData(3,4)
    print (r1)
    r2 = Rectangle()
    r2.setData(5,6)
    print (r2)
    print (r2.area())
