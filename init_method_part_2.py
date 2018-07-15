class Employee:
      def __init__(self, emp_name):
          self.name = emp_name
      def displayEmployeeName(self):
          print(self.name)

employee = Employee("Nick")
employee.displayEmployeeName()
