from datetime import datetime
from src.entities.Employee.PayrollRecord import *
from src.entities.Employee.Employee import *
from lib.CaseInsensitiveDict import CaseInsensitiveDict

class ViewModel:
    """ Queries entities to be used in ControllerView """
    def __init__(self, entity):
        self._entity = entity
        self._employeeFactoy = EmployeeFactory(entity.departments, entity.positions)
    
  
    def getEmployeeList(self):
        return self._entity.employees.getAllEmployees()


    def getEmployee(self, id):
        return self._entity.employees.getEmployee(id)
    
    def deleteEmployee(self, id):
        self.getEmployee(id).department.removeEmployee(id)
        self._entity.employees.deleteEmployee(id)
    
    def addEmployee(self, employee):
        allowance = 0
        
        if employee["position"] == "Manager":
            allowance = 5000
            
        if employee["position"] == "Assistant Manager":
            allowance = 3000
            
        newEmployee = self._employeeFactoy.create(employee["employeeNumber"], employee["lastName"], employee["firstName"], 
                 employee["position"], employee["department"], employee["birthdate"], employee["ratePerDay"], allowance)
        self._entity.employees.addEmployee(newEmployee)
        self._entity.saveState()


    def getMonthOfEmployeeRecords(self, employeeNumber):
        months = set()
        for record in self._entity.payrollRecords.getAllRecords():
            if record.employee.employeeNumber == employeeNumber:
                months.add(record.month)
        return months
    
    
    def increasePay(self, employeeNumber):
        employee = self.getEmployee(employeeNumber)
        employee.increasePay()
        self._entity.saveState()
    
    
    def increasePayAll(self):
        employees = self.getEmployeeList()
        for employee in employees:
            employee.increasePay()
        self._entity.saveState()
            
            
    def addPayrollRecord(self, payrollRecord):
        self._entity.payrollRecords.addRecord(payrollRecord)
        self._entity.saveState()


    def generatePayrollRecord(self, record):
        employee = record.employee
        
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        
        # Build ViewModel
        recordView                  = PayrollRecordEntityView()
        recordView.month            = months[record.month]
        recordView.employeeNumber   = employee.employeeNumber
        recordView.employeeName     = employee.lastName + ", " + employee.firstName
        recordView.department       = employee.department
        recordView.position         = employee.position
        recordView.ratePerDay       = employee.ratePerDay
        recordView.daysWorked       = record.daysWorked
        recordView.grossPay         = recordView.ratePerDay * record.daysWorked
        
        return recordView
        
    
        
    def generatePayrollRecordSingular(self, employeeNumber, month):
        currentRecord = self._entity.payrollRecords.getRecord(employeeNumber, month)
        return self.generatePayrollRecord(currentRecord)
        
    def generatePayrollRecordMonth(self, month):
        records = []
        for record in self._entity.payrollRecords.getAllRecords():
            if record.month == month:
                records.append(self.generatePayrollRecord(record))
        return records
    
    def generatePayrollRecordAll(self):
        records = []
        for record in self._entity.payrollRecords.getAllRecords():
            records.append(self.generatePayrollRecord(record))
        return records
    
    def getMonthRecords(self):
        months = set()
        for record in self._entity.payrollRecords.getAllRecords():
            months.add(record.month)
        return months
    
    
    def getDepartments(self):
        departments = CaseInsensitiveDict()
        originalDepartments = {"Accounting", "Human Resources", "Sales", "Marketing", "Manufacturing", "Admin"}
        for department in originalDepartments:
            departments[department] = department
        return departments
    
    
    def getPositions(self):
        positions = CaseInsensitiveDict()
        originalPositions = {"Manager", "Assistant Manager", "Secretary", "Staff"}        
        for position in originalPositions:
            positions[position] = position
        return positions
        
    
    def isPositionAvailable(self, department, position):
        positions = self.getPositions()
        position = positions[position]
        
        if position not in positions:
            return False
        
        if position not in self._entity.departments[department].getAvailablePositions():
            return False
        
        return True
        
        
        
    def getAvailablePositions(self, department):
        return self._entity.departments[department].getAvailablePositions()
        
    
    
    def getEmployeeNumbers(self):
        return {employee.employeeNumber for employee in self._entity.employees.getAllEmployees()}
    
    def getRecordEmployeeNumbers(self):
        return {record.employee.employeeNumber for record in self._entity.payrollRecords.getAllRecords()}
    
    def getRecordEmployeeNumbersForMonth(self, month):
        employeeNumbers = set()
        
        for record in self._entity.payrollRecords.getAllRecords():
            if record.month == month:
                employeeNumbers.add(record.employee.employeeNumber)
        
        return employeeNumbers
        

    
    
    