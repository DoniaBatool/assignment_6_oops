#9. Abstract Classes and Methods
#Assignment:
#Use the abc module to create an abstract class Shape with an abstract method area().
#Inherit a class Rectangle that implements area().

from abc import ABC,abstractmethod

class Shape(ABC):
     def __init__(self,l,b):
          self.length=l
          self.breadth=b
     @abstractmethod
     def area(self):
          pass
           

class Rectangle(Shape):
     def area(self):
          print(f"The area of the rectangle is {self.length * self.breadth} cm2")

R1 = Rectangle(5,10)
print(R1.length)
print(R1.breadth)
R1.area()
          