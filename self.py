'''
#TypeError: employeeDetails() takes no arguments (1 given)
class Employee:
      def employeeDetails():
          pass

employee = Employee()

employee.employeeDetails()
'''

class Employee:
      def employeeDetails(self):
          self.name = "Roy"
          print("Name: ",self.name)
          age = 30
          print("Age: ",age)
    
      def printEmployeeDetails(self):
          print("Printing in another function")
          print("Name: ",self.name)
          print("Age: ",age)

employee = Employee()

# python compiler pass the value using second way 
# that's is the reason we were getting error "takes no arguments 1 is needed" wheenver you define a method inside a class you need to pass one method

# (1) employee.employeeDetails()
# (2) Employee.employeeDetails(employee)

#this is short hand notification for 1st type
Employee.employeeDetails(employee)
employee.printEmployeeDetails()
# you will get an error NameError: global name 'age' is not defined
# this is becuase "name" variable is having lifecycle as long as object will be their
# as it is declared using self keyword, but this is not done with "age" varibale so its life
# cycle will be tell the scope of the that fucntion and "name" life cycle will be tell object is live 
