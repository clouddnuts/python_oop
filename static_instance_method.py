# instance VS static Method
class Employee:
      numberOfWorkingHours = 9
      def employeeDetails(self):
          self.name= "Roy"
      
      # using "static method" decorator
      @staticmethod
      def welcomeMessage():
          print("Hello World!!!")

employee = Employee()

# calling global variable, it will work
print(employee.numberOfWorkingHours)

# calling local variable from employeeDetails method
# it will thow an error :- AttributeError: Employee instance has no attribute 'name'
# you need to first initiate the method using object name

#print(employee.name)

# it will work as we have initialised using object name

employee.employeeDetails()
print(employee.name)   

# TypeError: welcomeMessage() takes no arguments (1 given)
# we use a decorator "@staticmethod" so that compliler will let to know that the object binding for this method has to be ingnored as this is a static method
employee.welcomeMessage()
 
