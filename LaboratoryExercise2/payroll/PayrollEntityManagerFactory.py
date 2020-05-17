from payroll.entities.filebound.FileBoundEmployeesEntity import FileBoundEmployeesEntity
from payroll.entities.filebound.FileBoundPayrollsEntity import FileBoundPayrollsEntity
from payroll.PayrollEntityManager import PayrollEntityManager
from lib.StringRowValueEncoder import StringRowValueEncoder
from lib.StringRowValueSplitter import StringRowValueSplitter
from data.FileDataHandler import FileDataHander
import os

class PayrollEntityManagerFactory:
    """ Factory class for PayrollEntityManager. Creates FileBoundEntities instead of normal entities """
    
    def create(self):
        cwd = os.getcwd()
        employeeEncoder = StringRowValueEncoder(",",";\n")
        employeeSplitter = StringRowValueSplitter(",",";")
        employeeFileHandler = FileDataHander(cwd + "\\data\\empList.txt")
        employee = FileBoundEmployeesEntity(employeeFileHandler, employeeSplitter, employeeEncoder)
        employee.retrieveState()
        
        payrollEncoder = StringRowValueEncoder(",",";\n")
        payrollSplitter = StringRowValueSplitter(",",";")
        payrollFileHandler = FileDataHander(cwd + "\\data\\empMR.txt")
        payrollRecords = FileBoundPayrollsEntity(payrollFileHandler, payrollSplitter, payrollEncoder)
        payrollRecords.retrieveState(employee)
        
        return PayrollEntityManager(employee, payrollRecords)
        