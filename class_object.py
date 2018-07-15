# check if an employee has achieved his weekly target or not
class Employee:
      name = "Ben"
      designation = "Sales Exexcutive"
      salesMadeThisWeek = 6

      def hasAchievedTarget(self):
          if self.salesMadeThisWeek >= 5:
             print("Target has been achieved")
          else:
             print("Target has not been achieved")



employeeOne = Employee()

employeeOne.hasAchievedTarget() 

print("Employee name",employeeOne.name)
print("Employee designation",employeeOne.designation)
print("Employee Sales made this week",employeeOne.salesMadeThisWeek)
