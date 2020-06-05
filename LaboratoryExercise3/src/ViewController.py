from datetime import datetime
from lib.Helper import *
from src.entities.Employee.Employee import *
from src.entities.Employee.PayrollRecord import *

class ViewController:
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
    
    
    def viewMenu(self, response = ""):
        
        menu = (
        "--------------------------------------------------------\n"\
        "  Malayan Colleges Laguna Employee Payroll System\n"\
        "--------------------------------------------------------\n"\
        "Value\tAction\n"\
        "-----\t------\n"\
        "  A\tDisplay Employee List\n"\
        "  B\tAdd Employee\n"\
        "  C\tUpdate Employee\n"\
        "  D\tIncrease Pay\n"\
        "  E\tAdd Payroll Record\n"\
        "  F\tGenerate Payroll Record\n"\
        "  X\tExit\n"\
        "--------------------------------------------------------"
        )
        
        print(menu)
        if response != None and response != "":
            print(">",response)
        
        selectionItems = {
            "a" : self.viewEmployeeList,
            "b" : self.viewAddEmployee,
            "c" : self.viewSelectUpdateEmployee,
            "d" : self.viewIncreasePay,
            "e" : self.viewAddPayrollRecord,
            "f" : self.viewGeneratePayrollRecord,
            "x" : exit
        }
        
        selection = selectionItems[inputComparator(message = "Please Enter One of the Values: ", 
                                                   errorMessage = "Please select one of the values.", 
                                                   comparator = multipleValidation((lambda x: x in selectionItems), self._selectionEmployeesNotNull), 
                                                   force_lower = True, strip = True)]
        response = selection()
        print()
        self.viewMenu(response)
        
        
    def viewEmployeeList(self):
        employees = self.model.getEmployeeList()
        # 0 - EmployeeID, 1 - First Name, 2 - Last Name, 3 - Department, 4 - Rate Per Hour
        employeeTable = [["ID:", "Last Name:", "First Name:", "Position:", "Department:", "Rate/Day:", "Allowance"]]
        for employee in employees:
            tableRow = [employee.employeeNumber, employee.lastName, employee.firstName, employee.position, employee.department.name, employee.ratePerDay, employee.allowance]
            employeeTable.append(tableRow)
        printAsTable(employeeTable)


    def viewSelectUpdateEmployee(self):
        if len(self.model.getRecordEmployeeNumbers()) == 0:
            return "There are no Records"
        self.viewEmployeeList()
        employeeNumber = inputComparator(message = "Enter Employee Number: ", 
                                         errorMessage = "Please Enter a Valid Employee Number.", 
                                         comparator = multipleValidation(self._validateExistingEmployeeNumber, self._existingEmployeeNumber, self._hasRecord), 
                                         strip = True)
        self.viewUpdateEmployee(employeeNumber)
        

    def viewUpdateEmployee(self, employeeNumber, response = ""):
        # Get Employee
        empEntity = self.model.getEmployee(employeeNumber)
        
        # Create Entity
        employee = {
            "employeeNumber"    : empEntity.employeeNumber,
            "lastName"          : empEntity.lastName,
            "firstName"         : empEntity.firstName,
            "birthdate"         : empEntity.birthdate,
            "department"        : empEntity.department.name,
            "position"          : empEntity.position,
            "ratePerDay"        : empEntity.ratePerDay,
        }
        menu = (
        f"--------------------------------------------------------\n"\
        f"  Malayan Colleges Laguna Employee Payroll System\n"\
        f"--------------------------------------------------------\n"\
        f"Value\tAction\n"\
        f"-----\t------\n"\
        f"  A\tLast Name: {empEntity.lastName}\n"\
        f"  B\tFirst Name: {empEntity.firstName}\n"\
        f"  C\tBirth Date: {empEntity.birthdate}\n"\
        f"  D\tDepartment: {empEntity.department.name}\n"\
        f"  E\tPosition: {empEntity.position}\n"\
        f"  F\tRate Per Day: {empEntity.ratePerDay}\n"\
        f"  X\tExit\n"\
        f"--------------------------------------------------------"
        )
        print(menu)
        
        if response != None and response != "":
            print(">",response)
            
        selectionItems = {'a', 'b', 'c', 'd', 'e', 'f', 'x'}
        selection = inputComparator(message = "Please Enter One of the Values: ", 
                                                   errorMessage = "Please select one of the values.", 
                                                   comparator = multipleValidation(lambda x: x in selectionItems), 
                                                   force_lower = True, strip = True)
        
        if selection == "x":
            return
        
        self.model.deleteEmployee(employeeNumber)
        # Populate Entity
        if selection == "a":
            employee["lastName"]       = inputComparator(message = "Enter Last Name: ", 
                                                  errorMessage = "Please Enter a Valid Last Name.", 
                                                  comparator = self._validateName, 
                                                  strip = True)
        if selection == "b":
            employee["firstName"]      = inputComparator(message = "Enter First Name: ", 
                                                  errorMessage = "Please Enter a Valid First Name.", 
                                                  comparator = self._validateName, 
                                                  strip = True)
        if selection == "c":
            birthYear =  inputNumber(message = "Enter Birth Year: ", 
                            errorMessage = "Please Enter a Valid Birth Year.", 
                            comparator = self._validateBirthYear, 
                            floatingPoint = False)
        
            birthMonth = inputNumber(message = "Enter Birth Month: ", 
                            errorMessage = "Please Enter a Valid Birth Month.", 
                            comparator = self._validateBirthMonth, 
                            floatingPoint = False)
        
            birthDay = inputNumber(message = "Enter Birth Day: ", 
                            errorMessage = "Please Enter a Valid Birth Day.", 
                            comparator = self._validateBirthDay(birthMonth), 
                            floatingPoint = False)
        
            employee["birthdate"] = datetime(year = birthYear, month = birthMonth, day = birthDay).strftime('%m-%d-%Y')
        if selection == "d":
            employee["department"]     = self.model.getDepartments()[inputComparator(message = "Available Departments: Accounting, Human Resources, Sales, Marketing, Manufacturing, Admin\nEnter Department: ", 
                                                                       errorMessage = "Please Enter a Valid Department.", 
                                                                       comparator = self._validateDepartment, 
                                                                       strip = True)]
        if selection == "e":
            availablePositions = self.model.getAvailablePositions(employee["department"])
            print("Available Positions: ", end = "")
            print(", ".join([position for position in availablePositions]))
        
            employee["position"]       = self.model.getPositions()[inputComparator(message = "Enter Position: ", 
                                                                       errorMessage = "Please Enter a Valid Position.", 
                                                                       comparator = self._validatePosition(employee["department"]), 
                                                                       strip = True)]     
        if selection == "f":
            employee["ratePerDay"]    = inputNumber(message = "Enter Rate Per Day: ", 
                                              errorMessage = "Please Enter a Valid Rate.", 
                                              comparator = self._validateRate, 
                                              floatingPoint = True)
        
        # Call Model
        self.model.addEmployee(employee)
        self.viewUpdateEmployee(employeeNumber, "Employee Updated")
                

    def viewAddEmployee(self):
        # Create Entity
        employee = {}
        
        # Populate Entity
        employee["employeeNumber"] = inputComparator(message = "Enter Employee Number: ", 
                                                  errorMessage = "Please Enter a Valid Employee Number.", 
                                                  comparator = self._validateNewEmployeeNumber, 
                                                  strip = True)
        employee["lastName"]       = inputComparator(message = "Enter Last Name: ", 
                                                  errorMessage = "Please Enter a Valid Last Name.", 
                                                  comparator = self._validateName, 
                                                  strip = True)
        employee["firstName"]      = inputComparator(message = "Enter First Name: ", 
                                                  errorMessage = "Please Enter a Valid First Name.", 
                                                  comparator = self._validateName, 
                                                  strip = True)
        
        birthYear =  inputNumber(message = "Enter Birth Year: ", 
                            errorMessage = "Please Enter a Valid Birth Year.", 
                            comparator = self._validateBirthYear, 
                            floatingPoint = False)
        
        birthMonth = inputNumber(message = "Enter Birth Month: ", 
                            errorMessage = "Please Enter a Valid Birth Month.", 
                            comparator = self._validateBirthMonth, 
                            floatingPoint = False)
        
        birthDay = inputNumber(message = "Enter Birth Day: ", 
                            errorMessage = "Please Enter a Valid Birth Day.", 
                            comparator = self._validateBirthDay(birthMonth), 
                            floatingPoint = False)
        
        employee["department"]     = self.model.getDepartments()[inputComparator(message = "Available Departments: Accounting, Human Resources, Sales, Marketing, Manufacturing, Admin\nEnter Department: ", 
                                                                       errorMessage = "Please Enter a Valid Department.", 
                                                                       comparator = self._validateDepartment, 
                                                                       strip = True)]
        availablePositions = self.model.getAvailablePositions(employee["department"])
        print("Available Positions: ", end = "")
        print(", ".join([position for position in availablePositions]))
        
        employee["position"]       = self.model.getPositions()[inputComparator(message = "Enter Position: ", 
                                                                       errorMessage = "Please Enter a Valid Position.", 
                                                                       comparator = self._validatePosition(employee["department"]), 
                                                                       strip = True)]     
        
        
        employee["birthdate"] = datetime(year = birthYear, month = birthMonth, day = birthDay).strftime('%m-%d-%Y')
        
        employee["ratePerDay"]    = inputNumber(message = "Enter Rate Per Day: ", 
                                              errorMessage = "Please Enter a Valid Rate.", 
                                              comparator = self._validateRate, 
                                              floatingPoint = True)
        
        # Call Model
        self.model.addEmployee(employee)
        return "Employee Added"
    
    
    def viewIncreasePay(self, response = ""):
        if len(self.model.getEmployeeList()) == 0:
            return "There are no Employees"
        
        menu =(
        "--------------------------------------------------------\n"\
        "  Malayan Colleges Laguna Employee Payroll System\n"\
        "--------------------------------------------------------\n"\
        "Increase Pay:\n"\
        "Value\tAction\n"\
        "-----\t------\n"\
        "  A\tIncrease Pay of All Employees\n"\
        "  B\tIncrease Pay of Specific Employee\n"\
        "  X\tBack\n"\
        "--------------------------------------------------------"
        )
        
        selectionItems = {
            'a' : self.viewIncreasePayAll,
            'b' : self.viewIncreasePaySingular,
            'x' : 'x'
        }
        
        print(menu)
        if response != None and response != "":
            print(">",response)
        
        selection = selectionItems[inputComparator(message = "Please Enter One of the Values: ", 
                                                   errorMessage = "Please select one of the values.", 
                                                   comparator = multipleValidation((lambda x: x in selectionItems), self._selectionEmployeesNotNull), 
                                                   force_lower = True, strip = True)]
        if selection == 'x':
            return
        response = selection()
        self.viewIncreasePay(response)
        
    
    def viewIncreasePayAll(self):
        self.model.increasePayAll()
        self.viewEmployeeList()
        return "Increased Pay of All Employees"
        
    
    def viewIncreasePaySingular(self):
        self.viewEmployeeList()
        employeeNumber = inputComparator(message = "Enter Employee Number: ", 
                                         errorMessage = "Please Enter a Valid Employee Number.", 
                                         comparator = multipleValidation(self._validateExistingEmployeeNumber, self._existingEmployeeNumber, self._hasRecord), 
                                         strip = True)
        oldPay = self.model.getEmployee(employeeNumber).ratePerDay
        self.model.increasePay(employeeNumber)
        newPay = self.model.getEmployee(employeeNumber).ratePerDay
        return f"Increased rate per day of {employeeNumber}. {oldPay} -> {newPay}"

    
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
        return "Payroll Record Added"
    
    
    def viewGeneratePayrollRecord(self, response = ""):
        if len(self.model.getRecordEmployeeNumbers()) == 0:
            return "There are no Records"
        
        menu =(
        "--------------------------------------------------------\n"\
        "  Malayan Colleges Laguna Employee Payroll System\n"\
        "--------------------------------------------------------\n"\
        "Generate Payroll Record:\n"\
        "Value\tAction\n"\
        "-----\t------\n"\
        "  A\tGenerate Payroll Record for Specific Employee\n"\
        "  B\tGenerate Payroll Records for Month\n"\
        "  C\tGenerate All Payroll Records\n"\
        "  X\tBack\n"\
        "--------------------------------------------------------"
        )
        
        selectionItems = {
            'a' : self.viewGeneratePayrollRecordSingular,
            'b' : self.viewGeneratePayrollRecordInMonth,
            'c' : self.viewGeneratePayrollRecordAll,
            'x' : 'x'
        }
        
        print(menu)
        if response != None and response != "":
            print(">",response)
        
        selection = selectionItems[inputComparator(message = "Please Enter One of the Values: ", 
                                                   errorMessage = "Please select one of the values.", 
                                                   comparator = multipleValidation((lambda x: x in selectionItems), self._selectionEmployeesNotNull), 
                                                   force_lower = True, strip = True)]
        if selection == 'x':
            return
        response = selection()
        print()
        self.viewGeneratePayrollRecord(response)

    
    def viewGeneratePayrollRecordSingular(self):
        self.viewEmployeeList()
        employeeNumber = inputComparator(message = "Enter Employee Number: ", 
                                         errorMessage = "Please Enter a Valid Employee Number.", 
                                         comparator = multipleValidation(self._validateExistingEmployeeNumber, self._existingEmployeeNumber, self._hasRecord), 
                                         strip = True)
        months = sorted(list(self.model.getMonthOfEmployeeRecords(employeeNumber)))
        print("Available Months: ", end = "")
        for month in months: 
            print(month, end = " ")
        print()
        month = inputNumber(message = "Enter Month: ", 
                            errorMessage = "Please Enter a Valid Month.", 
                            comparator = multipleValidation(self._validateMonth, self._hasRecordForMonth(employeeNumber)))
        
        payrollView = self.model.generatePayrollRecordSingular(employeeNumber, month)
        
        print(f"=================================================================\n"
              f"Payslip for the Month of {payrollView.month}\n"
              f"Employee No.: {payrollView.employeeNumber}\t\t\tEmployee Name: {payrollView.employeeName}\n"
              f"Department:   {payrollView.department.name}\t\tPosition: {payrollView.position}\n"
              f"Rate per Day: {payrollView.ratePerDay}\t\t\tNo. of Days Worked: {payrollView.daysWorked}\n"
              f"Gross Pay:    {payrollView.grossPay}\n"
              f"=================================================================")
    
    
    def viewGeneratePayrollRecordInMonth(self):
        months = sorted(list(self.model.getMonthRecords()))
        print("Months With Records: ", end = "")
        print(", ".join([str(m) for m in months]))
        month = inputNumber(message = "Enter Month: ", 
                            errorMessage = "Please Enter a Valid Month.", 
                            comparator = multipleValidation(self._validateMonth, self._monthHasRecord))
        
        payrollViews = self.model.generatePayrollRecordMonth(month)
        payrollTable = [["ID:", "Department:", "Position:", "Month:", "Rate Per Day:", "Number of Days Worked:", "Gross Pay:"]]
        
        for payrollView in payrollViews:
            tableRow = [payrollView.employeeNumber, payrollView.department.name,payrollView.position,  payrollView.month, payrollView.ratePerDay, payrollView.daysWorked, payrollView.grossPay]
            payrollTable.append(tableRow)
        printAsTable(payrollTable)
    
    
    def viewGeneratePayrollRecordAll(self):
        payrollViews = self.model.generatePayrollRecordAll()
        payrollTable = [["ID:", "Department:", "Position:", "Month:", "Rate Per Day:", "Number of Days Worked:", "Gross Pay:"]]
        
        for payrollView in payrollViews:
            tableRow = [payrollView.employeeNumber, payrollView.department.name,payrollView.position,  payrollView.month, payrollView.ratePerDay, payrollView.daysWorked, payrollView.grossPay]
            payrollTable.append(tableRow)
        printAsTable(payrollTable)
    
    
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
    
    
    def _monthHasRecord(self, value):
        months = self.model.getMonthRecords()
        if value not in months:
            print("Month has no record")
            return False
        return True
    
    
    def _validateName(self, value):
        """ Name must be characters only """
        if not value.isalpha():
            print("Name Must be Characters Only")
            return False
        return True
    
    
    def _validateDepartment(self, value):
        """ Department must one of the following: Accounting, Human Resources, Sales, Marketing, Manufacturing, Admin """
        departments = self.model.getDepartments()
        if value.lower() not in departments:
            print("Department must one of the following: Accounting, Human Resources, Sales, Marketing, Manufacturing, Admin")
            return False
        return True
    
    
    def _validateRate(self, value):
        """ Must be real number """
        if not (value >=0 and isNumber(value, floatingPoint = True)):
            print("Rate must be a positive real number")
            return False
        return True
    
    
    def _validateBirthdate(self, value):
        if not isValidDate(value, "%m-%d-%Y"):
            print("Please enter a valid date")
            return False
        return True
    
    
    def _validatePosition(self, department):
        def validate(value):
            positions = self.model.getPositions()
            if value.lower() not in positions:
                print("Position must one of the following: Manager, Assistant Manager, Secretary, Staff")
                return False
            if not self.model.isPositionAvailable(department, value):
                print("Position is not vacant")
                return False
            return True
        return validate
    
        
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
    
    
    def _validateBirthYear(self, val):
        try:
            datetime(year = val, month = 1, day = 1)
        except:
            return False
        else:
            return val >= 0
    
    
    def _validateBirthMonth(self, val):
        try:
            datetime(year = 2020, month = val, day = 1)
        except:
            return False
        else:
            return 12 >= val >= 1


    def _validateBirthDay(self, month):
        def validate(value):
            try:
                datetime(year = 2020, month = month, day = value)
            except:
                return False
            else:
                return isValidMonthDate(month, value)
        return validate
    
    def _noDelimiter(self, value):
        if ',' in value or ';' in value:
            return False
        return True