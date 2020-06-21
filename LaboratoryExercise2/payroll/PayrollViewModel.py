from datetime import datetime
from payroll.entities.PayrollRecordEntityView import PayrollRecordEntityView
from lib.CaseInsensitiveDict import CaseInsensitiveDict
import os

class PayrollViewModel:
    """ Queries entities to be used in ControllerView """
    def __init__(self, payrollEntityManager):
        self._entity = payrollEntityManager
        
        
    def getEmployeeList(self):
        return self._entity.employees.getAllEmployees()


    def getEmployee(self, id):
        return self._entity.employees.getEmployee(id)
    
    
    def addEmployee(self, employee):
        self._entity.employees.addEmployee(employee)
        self._entity.saveState()


    def getMonthOfEmployeeRecords(self, employeeNumber):
        months = set()
        for record in self._entity.payrollRecords.getAllRecords():
            if record.employee.employeeNumber == employeeNumber:
                months.add(record.month)
        return months
            
            
    def addPayrollRecord(self, payrollRecord):
        self._entity.payrollRecords.addRecord(payrollRecord)
        self._entity.saveState()


    def generatePayrollRecord(self, employeeNumber, month):
        currentRecord = self._entity.payrollRecords.getRecord(employeeNumber, month)
        employee = currentRecord.employee
        
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        
        # Build ViewModel
        recordView                  = PayrollRecordEntityView()
        recordView.month            = months[currentRecord.month]
        recordView.employeeNumber   = employee.employeeNumber
        recordView.employeeName     = employee.lastName + ", " + employee.firstName
        recordView.department       = employee.department
        recordView.ratePerDay       = employee.ratePerHour * 8
        recordView.daysWorked       = currentRecord.daysWorked
        recordView.grossPay         = recordView.ratePerDay * currentRecord.daysWorked
        
        return recordView
        
    
    def getDepartments(self):
        departments = CaseInsensitiveDict()
        originalDepartments = {"Accounting", "Marketing", "Human Resources", "Finance", "MIS", "Admin"}
        for department in originalDepartments:
            departments[department] = department
        return departments
    
        
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
    
    def generatePaySlip(self, payroll, payrollView):
        fileName = os.getcwd() + "/data/" + payrollView.employeeNumber + payrollView.month+".txt"
        with open(fileName, "w") as f:
            f.write(payroll)
            
        

    
    
    