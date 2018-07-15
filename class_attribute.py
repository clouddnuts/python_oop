class Employee:
      numberOfWorkingHours = 65

employeeOne = Employee()
employeeTwo = Employee()

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

# changing the class attribute using class name
Employee.numberOfWorkingHours = 75

# class attribute
print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

# changing the class attribute using instance name
employeeOne.numberOfWorkingHours = 45

print(employeeOne.numberOfWorkingHours) 
print(employeeTwo.numberOfWorkingHours)

#instance attribute
employeeOne.name = "Mark"
print(employeeOne.name)

employeeTwo.name = "Nick"
print(employeeTwo.name)

# SUMMARY
# first compiler checks instance attribute then it checks class attribute
