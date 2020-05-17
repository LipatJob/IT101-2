from payroll.entities.EmployeesEntity import EmployeesEntity
from payroll.entities.EmployeeEntity import EmployeeEntity
from payroll.entities.filebound.FileBound import FileBound

class FileBoundEmployeesEntity(EmployeesEntity, FileBound):
    def __init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy):
        EmployeesEntity.__init__(self)
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
        
    def toSerializable(self):
        """ Convert data into array """
        arr = []
        for val in super().getAllEmployees():
            tempArr = []
            tempArr.append(val.employeeNumber)
            tempArr.append(val.lastName)
            tempArr.append(val.firstName)
            tempArr.append(val.department)
            tempArr.append(val.ratePerHour)
            arr.append(tempArr)
        return arr  
    
    
    def setData(self, data):
        """ Set data from array """
        super().resetEmployees()
        for row in data:
            if len(row) == 1:
                continue
            # row[0] = id, row[1] = firstname, row[2] = lastname, row[3] = department, row[4] = ratePerHour
            tempEntity = EmployeeEntity()
            tempEntity.employeeNumber = row[0]
            tempEntity.firstName = row[1]
            tempEntity.lastName = row[2]
            tempEntity.department = row[3]
            tempEntity.ratePerHour = float(row[4])
            super().addEmployee(tempEntity)
        
        

        
    
    