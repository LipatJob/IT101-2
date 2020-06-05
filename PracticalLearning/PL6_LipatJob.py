# 2
class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)

# 3
# Accessing Attributes
"This would create first object of Employee Class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee Class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


# 4
emp1.name = "Zoraida" # Modify 'name' attribute
emp1.displayEmployee()
del emp1.name # Delete 'name' attribute
# emp1.displayEmployee()

hasattr(emp2, 'name')   # Returns True if 'age' attribute exists
getattr(emp2, 'name')   # Returns value of 'age' attribute
setattr(emp2, 'name', 'Manilyn') # Set attribute 'age' at 8
delattr(emp2, 'name')   # Delete attribute'age'