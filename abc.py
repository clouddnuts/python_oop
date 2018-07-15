#abc => Abstract Base Class
# By using abstact class you can force to a Class to use the method
# For ex- Shape is class is "abc", we have created area method in it, so its mandatory to use this method whenenver a new class is created
# if we try not to use area method of Shape class which us "ABC", it will thow an error
#  => TypeError: Can't instantiate abstract class Square with abstract methods area
#Also, we cannot create object of ABC class, we can only inherit to other classes 
from abc import ABCMeta, abstractmethod

 
class Shape(metaclass = ABCMeta):
      name = "RAHUL"
      @abstractmethod
      def area(self):
          return 0    
class Square(Shape):
      side = 5
      def area(self):
          print("AREA OF SQUARE: ",self.side * self.side)

class Rectangle(Shape):
      width = 5
      length = 10
      def area(self):
          print("AREA OF RECTANGLE: ",self.width * self.length)

square = Square()
rectangle = Rectangle()

rectangle.area()
square.area()


