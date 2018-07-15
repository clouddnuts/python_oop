# Polymorphism
# - the ablity of an entiy to be able to exist in more than one form
# Overriding -> Redefining the behavior of the base class method in a derived class
# Operator Overloading
# ABC  
class Employee:
      def setNumberOfWorkingHours(self):
          self.numberOfWorkingHours = 40

      def displayNumberOfWorkingHours(self):
           print(self.numberOfWorkingHours)

class Trainee(Employee):
      def setNumberOfWorkingHours(self):
          self.numberOfWorkingHours = 45

      # super keyword is used to override the vaule from child class to base classs
      def resetNumberOfWorkingHours(self):
          super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
employee.displayNumberOfWorkingHours()


trainee = Trainee()
trainee.setNumberOfWorkingHours()
trainee.displayNumberOfWorkingHours()

trainee.resetNumberOfWorkingHours()
trainee.displayNumberOfWorkingHours()

employee.displayNumberOfWorkingHours()
