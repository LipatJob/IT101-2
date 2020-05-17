class PayrollRecordEntityView:
    def __init__(self, month = "", employeeNumber = "", employeeName = "", 
                 department = "", ratePerDay = 0, daysWorked = 0, grossPay = 0):
        self.month = month
        self.employeeNumber = employeeNumber
        self.employeeName = employeeName
        self.department = department
        self.ratePerDay = ratePerDay
        self.daysWorked = daysWorked
        self.grossPay = grossPay