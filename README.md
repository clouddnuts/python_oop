CLASSES AND OBJECTS

1. What is a class ?

 A class is logical grouping of attributes(variables) and methods(functions)
 
 Syntax:
 
 class ClassName:
 # class body
 Example:
 class Employee:
 # class body
 
2. What is an object ?

 Object is an instance of a class that has access to all the attributes and methods of that class
 
 Syntax:
  objectName = ClassName()
 Example:
 employee = Employee()
 
 # The object employee now has access to all the
attributes and methods of the class Employee. You will be
learning more about attributes and methods in the next section.

3. What is object instantiation ?

The process of creation of an object of a class is called
instantiation
ATTRIBUTES AND METHODS

1. What are data members ?

Data members are attributes declared within a class. They
are properties that further define a class.
 There are two types of attributes: class attributes and
instance attributes.

2. What is a class attribute ?

An attribute that is common across all instances of a class is
called a class attribute.
 Class attributes are accessed by using class name as the
prefix.

Syntax:
 class className:
 classAttribute = value
 Example:
 class Employee:
 # This attribute is common across all instances of this
class
 numberOfEmployees = 0
employeeOne = E
3. What is an instance attribute ?
 
 An attribute that is specific to each instance of a class is
called an instance attribute.
 Instance attributes are accessed within an instance method
by making use of the self object.
 
 Syntax:
 class className:
 def methodName(self):
 self.instanceAttribute = value
 Example:
 class Employee:
 def employeeDetails(self, name):
 # name is the instance attribute
 self.name = name

4. What is the self parameter ?

Every instance method accepts has a default parameter that
is being accepted. By convention, this parameter is named self.
 The self parameter is used to refer to the attributes of that
instance of the class.
 Example:
 class Employee:
 def setName(self, name):
 self.name = name
employee = Employee()
 employee.setName('John')
 # The above statement is inferred as
Employee.setName(employee, 'John') where the object
employee is taken as the self argument.
 # In the init method when we say self.name, Python actually
takes it as employee.name, which is being stored with the value
John.

5. What are methods ?

A function within a class that performs a specific action is
called a method belonging to that class.
 Methods are of two types: static method and instance
method
6. What is an instance method ?
 A method which can access the instance attributes of a class
by making use of self object is called an instance method

Syntax:
 def methodName(self):
 # method body
 Example:
 class Employee:
 # employeeDetails() is the instance method
 def employeeDetails(self, name):
 self.name = name
7. What is a static method ?

A method that does not have access to any of the instance
attributes of a class is called a static method.
 Static method uses a decorator @staticmethod to indicate
this method will not be taking the default self parameter.

Syntax:
 @staticmethod
 # Observe that self is not being declared since this is a
static method
 def methodName():
 # method body
 Example:
 class Employee:
 numberOfEmployees = 0
 @StaticMethod
 def updateNumberOfEmployees():
 Employee.numberOfEmployees += 1
 employeeOne = Employee()
 employeeTwo = Employee()
 employeeOne.updateNumberOfEmployees()
 employeeTwo.updateNumberOfEmployees()
 print(Employee.numberOfEmployees)
 # We have used a static method that updates the class
attribute of the class Employee.
8. What are the ways to access the attributes and methods of a class ?
 Attributes and methods of a class can be accessed by
creating an object and accessing the attributes and objects
using class name or object name depending upon the type of
attribute followed by the dot operator (.) and the attribute name
or method name.
 Example:
 class Employee:
 numberOfEmployees = 0
 def printNumberOfEmployees(self):
 print(Employee.numberOfEmployees)
 employee = Employee()
 # Modify class attribute using dot operator
 Employee.numberOfEmployees += 1
 # Call the instance method using dot operator
 employee.printNumberOfEmployees()
9. What is an init method ?

An init method is the constructor of a class that can be used
to initialize data members of that class.
 It is the first method that is being called on creation of an 
object.

Syntax:
 def __init__(self):
 # Initialize the data members of the class
 Example:
 class Employee:
 def __init__(self):
 print("Welcome!")
 employee = Employee()
 # This would print Welcome! since __init__ method was
called on object instantiation.
ABSTRACTION AND ENCAPSULATION
1. What is encapsulation ?
 Hiding the implementation details from the end user is called
as encapsulation
2. What is abstraction ?
 Abstraction is the process of steps followed to achieve
encapsulation
INHERITANCE
1. What is inheritance ?
 Inheriting the attributes and methods of a base class into a
derived class is called Inheritance.
 Syntax:
 class BaseClass:
 # Body of BaseClass
 class DerivedClass(BaseClass):
 # Body of DerivedClass
 Example:
 class Shape:
 unitOfMeasurement = 'centimetre'
 class Square(Shape):
 def __init__(self):
 # The attribute unitOfMeasurement has been
inherited from the class Shape to this class Square
 print("Unit of measurement f
The Four Pillars of OOP in Python 3 for Beginners

 class derivedClass(baseClassOne, baseClassTwo):
 # Body of derived class
 Example:
 class OperatingSystem:
 multiTasking = True
 class Apple:
 website = 'www.apple.com'
 class MacOS(OperatingSystem, Apple):
 def __init__(self):
 if self.multiTasking is True:
 # The class MacOS has inherited 'multitasking'
attribute from the class OperatingSystem and 'website' attribute
from the class 'Apple'
 print("MacOS is a multitasking operating system.
Visit {} for more details".format(self.website))
 mac = MacOS()
3. What is multilevel inheritance ?
 Mechanism in which a derived class inherits from a base
class which has been derived from another base class is called
a multilevel inheritance
 Syntax:
 class BaseClass:
 # Body of baseClass
 class DerivedClassOne(BaseClass):
 # Body of DerivedClassOne
 class DerivedClassTwo(DerivedClassOne):
The Four Pillars of OOP in Python 3 for Beginners

 # Body of DerivedClassTwo
 Example:
 class Apple:
 website = 'www.apple.com'
 class MacBook(Apple):
 deviceType = 'notebook computer'
 class MacBookPro(MacBook):
 def __init__(self):
 # This class inherits deviceType from the base class
MacBook. It also inherits website from base class of MacBook,
which is Apple.
 print("This is a {}. Visit {} for more
details".format(self.deviceType, self.website))
 macBook = MacBookPro()
 
5. What is an abstract base class ?

A base class which contains abstract methods that are to
be overridden in its derived class is called an abstract base
class. They belong to the abc module.
Example:
from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCMeta):
@abstractmethod
def area(self):
return 0
class Square(Shape):
def area(self, side)
return side * side
The Four Pillars of OOP in Python 3 for Beginners

6. What are the naming conventions used for private,
protected and public members ?

Private -> __memberName
Protected -> _memberName
Public -> memberName

7. How is name mangling done for private members by
Python ?
Name mangling is done by prepending the member name
with an underscore and class name.
_className__memberName
POLYMORPHISM

1. What is polymorphism ?
 The same interface existing in different forms is called
polymorphism
 Example :
 An addition between two integers 2 + 2 return 4
whereas an addition between two strings "Hello" + "World"
concatenates it to "Hello World"
2. What is operator overloading ?
 Redefining how an operator operates its operands is called
operator overloading.
 Syntax:
 def __operatorFunction__(operandOne, operandTwo):
 # Define the operation that has to be performed
 Example:
 class Square:
 def __init__(self, side):
 self.side = side
 def __add__(sideOne, sideTwo):
 return(sideOne.side + sideTwo.side)
 squareOne = Square(10)
 squareTwo = Square(20)
 # After overloading __add__ method, squareOne +
squareTwo is interpreted as Square.__add__(squareOne,
squareTwo)
 print("Sum of sides of two squares = ", squareOne +
squareTwo)
The Four Pillars of OOP in Python 3 for Beginners

3. What is overriding ?
 Modifying the inherited behaviour of methods of a base class
in a derived class is called overriding.
 Syntax:
 class BaseClass:
 def methodOne(self):
 # Body of method
 class DerivedClass(baseClass):
 def methodOne(self):
 # Redefine the body of methodOne
 Example:
 class Shape:
 def area():
 return 0
 class Square(Shape):
 def area(self, side):
 return (side * side)
 
4. Why is super() used ?
 super() is used to access the methods of base class.
 Example:
 class BaseClass:
 def baseClassMethod():
 print("This is BaseClassOne")
 class DerivedClass(BaseClass):
 def __init__(self):
 # calls the base class method
 super().baseClassMethod()
