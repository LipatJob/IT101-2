from lib.Helper import *
from payroll.entities.EmployeeEntity import EmployeeEntity
from payroll.entities.PayrollRecordEntity import PayrollRecordEntity

class PayrollViewController:
    """ The class where the User Interface is handled
    
    Args
    ----
    payrollModel : PayrollViewModel
        Where the program queries the needed data
    
    Attributes
    ----------
    model : PayrollViewModel
        Where the program queries the needed data
        
    """
    def __init__(self, payrollModel):
        self.model = payrollModel
    
    
    def viewMenu(self):
        menu =(
        "--------------------------------------------------------\n"\
        "  Malayan Colleges Laguna Employee Payroll System\n"\
        "--------------------------------------------------------\n"\
        "Value\tAction\n"\
        "-----\t------\n"\
        "  A\tDisplay Employee List\n"\
        "  B\tAdd Employee\n"\
        "  C\tAdd Payroll Record\n"\
        "  D\tGenerate Payroll Record\n"\
        "  X\tExit\n"\
        "--------------------------------------------------------"
        )
        selectionItems = {
            "a" : self.viewEmployeeList,
            "b" : self.viewAddEmployee,
            "c" : self.viewAddPayrollRecord,
            "d" : self.viewGeneratePayrollRecord,
            "x" : exit
        }
        
        print(menu)
        selection = selectionItems[inputComparator(message = "Please Enter One of the Values: ", 
                                                   errorMessage = "Please select one of the values.", 
                                                   comparator = multipleValidation((lambda x: x in selectionItems), self._selectionEmployeesNotNull), 
                                                   force_lower = True, strip = True)]
        selection()
        print()
        self.viewMenu()
        
        
    def viewEmployeeList(self):
        employees = self.model.getEmployeeList()
        # 0 - EmployeeID, 1 - First Name, 2 - Last Name, 3 - Department, 4 - Rate Per Hour
        for employee in employees:
            print(f"ID: {employee.employeeNumber}\tName: {employee.lastName}, {employee.firstName}\tDepartment: {employee.department}\tRate/Hour: {employee.ratePerHour}")


    def viewAddEmployee(self):
        # Create Entity
        employee = EmployeeEntity()
        
        # Populate Entity
        employee.employeeNumber = inputComparator(message = "Enter Employee Number: ", 
                                                  errorMessage = "Please Enter a Valid Employee Number.", 
                                                  comparator = self._validateNewEmployeeNumber, 
                                                  strip = True)
        employee.lastName       = inputComparator(message = "Enter Last Name: ", 
                                                  errorMessage = "Please Enter a Valid Last Name.", 
                                                  comparator = self._validateName, 
                                                  strip = True)
        employee.firstName      = inputComparator(message = "Enter First Name: ", 
                                                  errorMessage = "Please Enter a Valid First Name.", 
                                                  comparator = self._validateName, 
                                                  strip = True)
        employee.department     = self.model.getDepartments()[inputComparator(message = "Available Departments: Accounting, Marketing, Human Resources, Finance, MIS, Admin\nEnter Department: ", 
                                                                       errorMessage = "Please Enter a Valid Department.", 
                                                                       comparator = self._validateDepartment, 
                                                                       strip = True)]
        employee.ratePerHour    = inputNumber(message = "Enter Rate Per Hour: ", 
                                              errorMessage = "Please Enter a Valid Rate.", 
                                              comparator = self._validateRate, 
                                              floatingPoint = True)
        
        # Call Model
        self.model.addEmployee(employee)
        print("Employee Added")
    
    
    def viewAddPayrollRecord(self):
        # Create Entity
        payrollRecord = PayrollRecordEntity()
        
        self.viewEmployeeList()
        # Populate Entity
        payrollRecord.employee = self.model.getEmployee(inputComparator(message = "Enter Employee Number: ",
                                                                        errorMessage = "Please Enter a Valid Employee Number.", 
                                                                        comparator = multipleValidation(self._validateExistingEmployeeNumber, self._notFullRecord), 
                                                                        strip = True))
        # Get the set difference of all the months and the months the employee has 
        availableMonths = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} - self.model.getMonthOfEmployeeRecords(payrollRecord.employee.employeeNumber)
        print("Available Months: ", end = "")
        for month in availableMonths: 
            # Display all available months
            print(month, end = " ")
        print()
        payrollRecord.month          = inputNumber(message = "Enter Month: ", 
                                                   errorMessage = "Please Enter a Valid Month.", 
                                                   comparator = multipleValidation(self._validateMonth, self._notFullRecord, self._noRecordExists(payrollRecord.employee.employeeNumber)))
        payrollRecord.daysWorked     = inputNumber(message = "Enter Days Worked: ", 
                                                   errorMessage = "Please Enter Valid Days Worked.", 
                                                   comparator = self._validateDaysWorked(payrollRecord.month))
        
        # Call Model
        self.model.addPayrollRecord(payrollRecord)
        print("Payroll Record Added")
    
    def viewGeneratePayrollRecord(self):
        if len(self.model.getRecordEmployeeNumbers()) == 0:
            print("There are no Records")
            return
        
        self.viewEmployeeList()
        employeeNumber = inputComparator(message = "Enter Employee Number: ", 
                                         errorMessage = "Please Enter a Valid Employee Number.", 
                                         comparator = multipleValidation(self._validateExistingEmployeeNumber, self._existingEmployeeNumber, self._hasRecord), 
                                         strip = True)
        months = self.model.getMonthOfEmployeeRecords(employeeNumber)
        print("Available Months: ", end = "")
        for month in months: print(month, end = " ")
        print()
        month = inputNumber(message = "Enter Month: ", 
                            errorMessage = "Please Enter a Valid Month.", 
                            comparator = multipleValidation(self._validateMonth, self._hasRecordForMonth(employeeNumber)))
        
        payrollView = self.model.generatePayrollRecord(employeeNumber, month)
        
        payslip = (f"=================================================================\n"
                   f"Payslip for the Month of {payrollView.month}\n"
                   f"Employee No.: {payrollView.employeeNumber}\t\tEmployee Name: {payrollView.employeeName}\n"
                   f"Department:   {payrollView.department}\n"
                   f"Rate per Day: {payrollView.ratePerDay}\t\t\tNo. of Days Worked: {payrollView.daysWorked}\n"
                   f"Gross Pay:    {payrollView.grossPay}\n"
                   f"=================================================================")
        self.model.generatePaySlip(payslip, payrollView)
        print("\nPayslip Generated")
        print(payslip)
    
    
    # VALIDATORS    
    def _selectionEmployeesNotNull(self, value):
        if(value == 'b'):
            return True
        
        if len(self.model.getEmployeeList()) == 0:
            print("There are No Employees")
            return False
        return True
    
    
    def _validateNewEmployeeNumber(self, value):
        """ Employee Number must be 9 digits """
        if len(value) != 9:
            print("Employee Number Must be 9 digits")
            return False
        
        for digit in value:
            if not isNumber(digit):
                print("Employee Number May Only Contain Numbers")
                return False
        
        if value in self.model.getEmployeeNumbers():
            print("Please Enter a Unique Employee Number")
            return False
        
        return True
    
    
    def _validateExistingEmployeeNumber(self, value):
        """ Employee Number must be 9 digits """
        if len(value) != 9:
            print("Employee Number Must be 9 digits")
            return False
        
        for digit in value:
            if not isNumber(digit):
                print("Employee Number May Only Contain Numbers")
                return False
        
        if value not in self.model.getEmployeeNumbers():
            print("Please Enter an ID of an Existing Employee")
            return False
        
        return True
    
    
    def _noRecordExists(self, employeeNumber):
        """ Employe Should have no record for the month """
        monthEmployeeRecords = self.model.getMonthOfEmployeeRecords(employeeNumber)
        
        def validate(month):    
            if month in monthEmployeeRecords:
                print("Employee Must Have No Record for the selected Month")
                return False
            return True
        
        return validate

    
    def _validateName(self, value):
        """ Name must be characters only """
        if len(value) == 0:
            return False
        if not isAlphaOrSpace(value):
            print("Name Must be Characters Only")
            return False
        return True
    
    
    def _validateDepartment(self, value):
        """ Department must one of the following: Accounting, Marketing, Human Resources, Finance, MIS, Admin """
        departments = self.model.getDepartments()
        if value.lower() not in departments:
            print("Department must one of the following: Accounting, Marketing, Human Resources, Finance, MIS, Admin")
            return False
        return True
    
    
    def _validateRate(self, value):
        """ Must be real number """
        if not (value >=0 and isNumber(value, floatingPoint = True)):
            print("Rate must be a positive real number")
            return False
        return True
    
    
    def _existingEmployeeNumber(self, value):
        """  """
        employeeNumbers = self.model.getEmployeeNumbers()
        if value not in employeeNumbers:
            print("")
            return False
        return True
    
    
    def _validateMonth(self, value):
        if value > 12 or value < 1:
            print("Please Enter a Value from 1 to 12")
            return False
        if not isWhole(value):
            print("Please Enter a Whole Number")
            return False
        
        return True
    
    
    def _validateDaysWorked(self, month):
        """         jan  feb mar apr may jun jul aug sep oct nov dec"""
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = month - 1
        def validate(days):
            if not isWhole(days) or days > monthDays[month] or days < 1:
                print(f"Please Enter a Number From 1 to {monthDays[month]}")
                return False
            return True
        
        return validate
    
    
    def _hasRecord(self, employeeNumber):
        """ Employee Must Have Existing Recod """
        records  = self.model.getRecordEmployeeNumbers()
        
        if employeeNumber not in records:
            print("Employee Must Have Existing Record")
            return False
        return True
    
    
    def _hasRecordForMonth(self, employeeNumber):
        """ Employee Must Have Existing Record for the Month """
        def validate(month):
            if employeeNumber not in self.model.getRecordEmployeeNumbersForMonth(month):
                print("Employee Must Have Existing Record for the Month")
                return False
            return True
        
        return validate
        
    
    def _notFullRecord(self, id):
        """ Employee must not have a full record"""
        if len(self.model.getMonthOfEmployeeRecords(id)) == 12:
            print("Current Employee has full records")
            return False
        return True
    
    