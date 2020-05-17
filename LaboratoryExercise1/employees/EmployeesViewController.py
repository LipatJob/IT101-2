from employees.Helper import inputComparator, inputNumber, notblank

class EmployeesViewController:
    """The class where the User Interface is handled
    
    Args
    ----
    employeesModel : EmployeesViewModel
        model to de injected
    
    Attributes
    ----------
    model : EmployeesViewModel
        where the needed data is queried
        
    """
    def __init__(self, employeesModel):
        self.model = employeesModel # type: EmployeesModel
    
    def viewMenu(self):
        menu = """--------------------------------------------------------
  Malayan Colleges Laguna Employee Information System
--------------------------------------------------------
Value\tAction
-----\t------
  A\tDisplay the Number of Employees
  B\tFilter Employees by Given Age Range (in years)
  C\tFilter Employees by Given City
  D\tCount Employees in Given County
  E\tCount Employees using Given Email Provider Site 
  X\tExit
--------------------------------------------------------"""
        selectionItems = {
            "a" : self.viewEmployeeCount,
            "b" : self.viewFilterEmployeeAgeRange,
            "c" : self.viewFilterEmployeeCity,
            "d" : self.viewCountEmployeePerCounty,
            "e" : self.viewCountEmployeePerEmailProvider,
            "x" : exit
        }
        print(menu)
        selection = selectionItems[inputComparator("Please Enter One of the Values: ", "Please select one of the values.", (lambda x: x in selectionItems), force_lower = True, strip = True)]
        selection()
        print()
        self.viewMenu()
        
        
    def viewEmployeeCount(self):
        # Call Model
        employeeCount = self.model.employeeCount()['EmployeeCount']
        print()
        # Bind Model to UI
        print(f">> Number of Employees: {employeeCount}")
    
    def isValidMaxAge(self, minAge, maxAge):
        """ Validate whether the maximum age is valid """
        if minAge > maxAge:
            print("Maximum Age Must be Greater Than or Equal to the Minimum Age")
            return False
        return True
    
    def viewFilterEmployeeAgeRange(self):
        # Input Age Range
        minAge = inputNumber("Enter Mimimum Age: ", "Please Enter a Valid Minimum Age.", lambda inVal : inVal >= 0)
        maxAge = inputNumber("Enter Maximum Age: ", "Please Enter a Valid Maximum Age.", lambda inVal : self.isValidMaxAge(minAge, inVal))
        print()
        
        # Call Model
        filteredEmployees = self.model.filterEmployeeAgeRange(minAge, maxAge)["Employees"]
        
        # Bind Model to UI
        if len(filteredEmployees) == 0:
            print(f">> There are No Employees with Ages Between and Including {minAge} and {maxAge}")
        else:
            print(f">> Employees with Ages Between and Including {minAge} and {maxAge}")
            for index, employee in enumerate(filteredEmployees):
                print(f'>> {index + 1}. Name: {employee["last_name"]}, {employee["first_name"]}\t||\tAge: {employee["age"]}')
            
    
    def viewFilterEmployeeCity(self):
        # Display Available Cities
        cities = self.model.getCities()
        print("Available Cities: ")
        for city in sorted(cities):
            print(city, end = ", ")
        print()
        
        # Input City
        inputCity = inputComparator("Enter City: ", "Please Enter a valid City.", comparator = notblank,strip = True)
        print()
        
        # Call Model
        modelData = self.model.filterEmployeeCity(inputCity)
        filteredEmployees = modelData["Employees"]
        originalCity = modelData["City"]
        
        # Bind Model To UI
        if len(filteredEmployees) == 0:
            print(f">> There are No Employees Residing in {originalCity}")
        else:
            print(f">> Employees Residing in the City of {originalCity}: ")
            for index, employee in enumerate(filteredEmployees):
                print(f'>> {index + 1}. \tName: {employee["last_name"]}, {employee["first_name"]}\t||\tCity: {employee["city"]}')

               
    def viewCountEmployeePerCounty(self):
        # Display Available Counties
        counties = self.model.getCounties()
        print("Available Countries: ")
        for county in sorted(counties):
            print(county, end = ", ")
        print()
        
        # Input County
        inputCounty = inputComparator("Enter County: ", "Please Enter a valid County.", comparator = notblank,strip = True)
        print()
        
        # Call Model
        modelData = self.model.countEmployeeCounty(inputCounty)
        employeeCount = modelData["Count"]
        originalCounty = modelData["County"]
        
        # Bind Model To UI
        if employeeCount == 0:
            print(f">> There are No Employees in {originalCounty}")
        else:
            print(f">> Number of Employees in {originalCounty}: {employeeCount}")
    
    
    def viewCountEmployeePerEmailProvider(self):
        # Display Available Email Providers
        emailProviders = self.model.getEmailProviers()
        print("Available Email Providers: ")
        for emailProvider in sorted(emailProviders):
            print(emailProvider, end = ", ")
        print()
        
        # Input Email Provider
        inputEmailProvider = inputComparator("Enter Email Provider: ", "Please Enter a valid Email Provider.", comparator = notblank, strip = True)
        print()
        
        # Call Model
        modelData = self.model.countEmployeeEmailProvider(inputEmailProvider)
        employeeCount = modelData["Count"]
        originalEmailProvider = modelData["EmailProvider"]
        
        # Bind Model To UI
        if employeeCount == 0:
            print(f">> There are No Employees Using '{originalEmailProvider}' as Email Provder")
        else:
            print(f">> Number of Employees Using '{originalEmailProvider}' as Email Provider: {employeeCount}")
    