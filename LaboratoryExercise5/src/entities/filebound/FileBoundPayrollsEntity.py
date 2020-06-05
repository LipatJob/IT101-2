from payroll.entities.PayrollRecordsEntity import PayrollRecordsEntity
from payroll.entities.PayrollRecordEntity import PayrollRecordEntity
from payroll.entities.filebound.FileBound import FileBound

class FileBoundPayrollsEntity(PayrollRecordsEntity, FileBound):
    def __init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy):
        PayrollRecordsEntity.__init__(self)
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
        
    
    def toSerializable(self):
        """ Convert data into array """
        arr = []
        for val in super().getAllRecords():
            tempArr = []
            tempArr.append(val.employee.employeeNumber)
            tempArr.append(val.month)
            tempArr.append(val.daysWorked)
            arr.append(tempArr)
        return arr    
    
    
    def setData(self, data, employeesEntity):
        """ Set data from array"""
        super().resetRecords()
        for row in data:
            if len(row) == 1:
                continue
            # row[0] = id, row[1] = month, row[2] = daysworked
            tempEntity = PayrollRecordEntity()
            tempEntity.employee = employeesEntity.getEmployee(row[0])
            tempEntity.month = int(row[1])
            tempEntity.daysWorked = int(row[2])
            super().addRecord(tempEntity)     
    

    def retrieveState(self, employeesEntity):
        """ Override to allow creation of relationship """
        dataString = self.fileHandler.readData()
        dataArray = self.dataParsingStrategy.parse(dataString)
        self.setData(dataArray, employeesEntity)