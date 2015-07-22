import math

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x;
        self.y = y;

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

class Line:

    def __init__(self, start, end):
        self.start = start;
        self.end = end;

    def __str__(self):
        return "The line consists of the points: %s and %s" % (self.start, self.end)

    def length(self):
        return math.sqrt((self.end.x - self.start.x)**2 + (self.end.y- self.start.y )**2)
   
if __name__ == "__main__":
    
    emptyPoint = Point()
    print(emptyPoint)
    
    firstNonEmptyPoint = Point(1,3)
    print(firstNonEmptyPoint)

    secondNonEmptyPoint = Point(8,42)
    print(secondNonEmptyPoint)

    thirdNonEmptyPoint = Point(4,123)
    print(firstNonEmptyPoint)

    fourthNonEmptyPoint = Point(45,648)
    print(secondNonEmptyPoint)

    firstLine = Line(firstNonEmptyPoint, secondNonEmptyPoint)
    print(firstLine)

    print(firstLine.length())

    secondLine = Line(thirdNonEmptyPoint, fourthNonEmptyPoint)
    print(secondLine)

    print(secondLine.length())
    

"""------------------------------Output------------------------------
(0, 0)
(1, 3)
(8, 42)
(1, 3)
(8, 42)
The line consists of the points: (1, 3) and (8, 42)
39.6232255123179
The line consists of the points: (4, 123) and (45, 648)
526.598518797765
"""


        
