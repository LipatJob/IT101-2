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