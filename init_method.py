class Employee:
      # as soon "employee" object in created this method will be the first method to be called
      # this will initialise all the instance variable mentioned in the block of it
      # this will make all varaible fully intitalisedi
      # now we don't need "enterEmployeeDeatials" method

      def __init__(self):
          self.name = "Mark"

      '''
      def enterEmployeeDetails(self):
          self.name = "Mark"
      '''

      def displayEmployeeName(self):
          print(self.name)


employee = Employee()

# AttributeError: Employee instance has no attribute 'name'
# this means this method is not initialised, so we need to call enterEmployeeDetails before it

employee.displayEmployeeName()




