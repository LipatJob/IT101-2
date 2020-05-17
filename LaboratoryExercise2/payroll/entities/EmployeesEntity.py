class EmployeesEntity:
    def __init__(self):
        self._employees = {}
    
    def addEmployee(self, employee):
        self._employees[employee.employeeNumber] = employee
    
    def getEmployee(self, id):
        return self._employees[id]
    
    def getAllEmployees(self):
        return self._employees.values()
    
    def resetEmployees(self):
        self._employees = {}
    
    
    
    
    