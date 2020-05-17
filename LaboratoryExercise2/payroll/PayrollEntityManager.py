class PayrollEntityManager:
    """ Contains the entities and their relationships """
    def __init__(self, employees, payrollRecords):
        self.employees = employees
        self.payrollRecords = payrollRecords
    
    def saveState(self):
        self.employees.saveState()
        self.payrollRecords.saveState()
        
    def retrieveState(self):
        self.employees.retrieveState()
        self.payrollRecords.retrieveState(self.employees)
    

        