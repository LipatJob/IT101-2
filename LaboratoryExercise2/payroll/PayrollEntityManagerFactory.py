from payroll.entities.filebound.FileBoundEmployeesEntity import FileBoundEmployeesEntity
from payroll.entities.filebound.FileBoundPayrollsEntity import FileBoundPayrollsEntity
from payroll.PayrollEntityManager import PayrollEntityManager
from payroll.filestrategy.FileEncoder import FileEncoder
from payroll.filestrategy.FileParser import FileParser
from data.FileDataHandler import FileDataHander
import os

class PayrollEntityManagerFactory:
    """ Factory class for PayrollEntityManager. Creates FileBoundEntities instead of normal entities """
    
    def create(self):
        cwd = os.getcwd()
        employeeEncoder = FileEncoder(",",";\n")
        employeeSplitter = FileParser(",",";")
        employeeFileHandler = FileDataHander(cwd + "\\data\\empList.txt")
        employee = FileBoundEmployeesEntity(employeeFileHandler, employeeSplitter, employeeEncoder)
        employee.retrieveState()
        
        payrollEncoder = FileEncoder(",",";\n")
        payrollSplitter = FileParser(",",";")
        payrollFileHandler = FileDataHander(cwd + "\\data\\empMR.txt")
        payrollRecords = FileBoundPayrollsEntity(payrollFileHandler, payrollSplitter, payrollEncoder)
        payrollRecords.retrieveState(employee)
        
        return PayrollEntityManager(employee, payrollRecords)
        