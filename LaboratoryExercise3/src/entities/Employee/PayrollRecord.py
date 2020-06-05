from lib.FileBound import FileBound
from lib.FileBound import FileBound
from lib.filestrategy.FileEncoder import FileEncoder
from lib.filestrategy.FileDecoder import FileDecoder
from lib.FileDataHandler import FileDataHandler
import os


class PayrollRecordEntity:
    def __init__(self, employee = None, month = 0, daysWorked = 0):
        self.employee = employee
        self.month = month
        self.daysWorked = daysWorked
        
        
class PayrollRecordEntityView:
    def __init__(self, month = "", employeeNumber = "", employeeName = "", 
                 department = "", position = "", ratePerDay = 0, daysWorked = 0, grossPay = 0):
        self.month = month
        self.employeeNumber = employeeNumber
        self.employeeName = employeeName
        self.department = department
        self.position = position
        self.ratePerDay = ratePerDay
        self.daysWorked = daysWorked
        self.grossPay = grossPay
        
        
class PayrollRecordsEntity:
    def __init__(self):
        self._records = []
    
    def addRecord(self, record):
        self._records.append(record)
        
    def getRecord(self, employeeNumber, month):
        for record in self._records:
            if record.employee.employeeNumber == employeeNumber and record.month == month:
                return record
        return None
        
    def getAllRecords(self):
        return self._records
    
    def resetRecords(self):
        self._records = []
    

class FileBoundPayrollsEntityFactory:
    def create(self, employees):
        cwd = os.getcwd()
        encoder = FileEncoder(",",";\n")
        decoder = FileDecoder(",",";")
        fileHandler = FileDataHandler(cwd + "\\data\\payrollRecord.txt")
        return FileBoundPayrollsEntity(fileHandler, decoder, encoder, employees)
        
    
class FileBoundPayrollsEntity(PayrollRecordsEntity, FileBound):
    def __init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy, employees):
        PayrollRecordsEntity.__init__(self)
        FileBound.__init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy)
        self.employees = employees
    
    def toSerializable(self):
        """ Convert data into array """
        arr = []
        for val in self._records:
            tempArr = []
            tempArr.append(val.employee.employeeNumber)
            tempArr.append(val.month)
            tempArr.append(val.daysWorked)
            arr.append(tempArr)
        return arr    
    
    
    def setData(self, data):
        """ Set data from array"""
        self._records = []
        for row in data:
            if len(row) == 1:
                continue
            # row[0] = id, row[1] = month, row[2] = daysworked
            tempEntity = PayrollRecordEntity()
            tempEntity.employee = self.employees.getEmployee(row[0])
            tempEntity.month = int(row[1])
            tempEntity.daysWorked = int(row[2])
            self._records.append(tempEntity)