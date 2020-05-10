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
        menu = """A. Number of Employees
B. Filter Employees by Given Age Range (in years)
C. Filter Employees by Given City
D. Count Employees in Given County
E. Count Employees using Given Email Provider Site 
X. Exit"""
        selectionItems = {
            "a" : self.viewEmployeeCount,
            "b" : self.viewFilterEmployeeAgeRange,
            "c" : self.viewFilterEmployeeCity,
            "d" : self.viewCountEmployeePerCounty,
            "e" : self.viewCountEmployeePerEmailProvider,
            "x" : exit
        }
        print(menu)
        selection = selectionItems[inputComparator("Enter a value: ", "Please select one of the values", (lambda x: x in selectionItems), force_lower = True)]
        selection()
        print()
        self.viewMenu()
        
        
    def viewEmployeeCount(self):
        # Call Model
        employeeCount = self.model.employeeCount()['EmployeeCount']
        
        # Bind Model to UI
        print(f"Number of employees: {employeeCount}")
    
    
    def viewFilterEmployeeAgeRange(self):
        # Input Age Range
        print("Enter age range: ")
        minAge = inputNumber("Input Mimimum Age: ", "Please Enter a valid minimum age", lambda inVal : inVal >= 0)
        maxAge = inputNumber("Input Maximum Age: ", "Please Enter a valid maximum age", lambda inVal : inVal >= minAge)
        
        # Call Model
        filteredEmployees = self.model.filterEmployeeAgeRange(minAge, maxAge)["Employees"]
        
        # Bind Model to UI
        if len(filteredEmployees) == 0:
            print(f"There are no employees between and including {minAge} and {maxAge}")
        else:
            print(f"Employees with ages between and including {minAge} and {maxAge}:")
            for index, employee in enumerate(filteredEmployees):
                print(str(index + 1) + ".")
                print("Last Name:", employee["last_name"])
                print("First Name:", employee["first_name"])
                print("Age:", employee["age"])
                print("--------------------------------")
            
    
    def viewFilterEmployeeCity(self):
        # Display Available Cities
        cities = self.model.getCities()
        print("Available Cities: ")
        for city in cities:
            print(city, end = ", ")
        print()
        
        # Input City
        inputCity = inputComparator("Enter City: ", "Please Enter a valid City", comparator = notblank)
        print()
        
        # Call Model
        modelData = self.model.filterEmployeeCity(inputCity)
        filteredEmployees = modelData["Employees"]
        originalCity = modelData["City"]
        
        # Bind Model To UI
        if len(filteredEmployees) == 0:
            print(f"There are no employees residing in {originalCity}")
        else:
            print(f"Employees residing in the city of {originalCity}: ")
            for index, employee in enumerate(filteredEmployees):
                print(str(index + 1) + ".")
                print("Last Name:", employee["last_name"])
                print("First Name:", employee["first_name"])
                print("City:", employee["city"])
                print("--------------------------------")

               
    def viewCountEmployeePerCounty(self):
        # Display Available Counties
        counties = self.model.getCounties()
        print("Available Countries: ")
        for county in counties:
            print(county, end = ", ")
        print()
        
        # Input County
        inputCounty = inputComparator("Enter County: ", "Please Enter a valid County", comparator = notblank)
        print()
        
        # Call Model
        modelData = self.model.countEmployeeCounty(inputCounty)
        employeeCount = modelData["Count"]
        originalCounty = modelData["County"]
        
        # Bind Model To UI
        if employeeCount == 0:
            print(f"There are no employees in {originalCounty}")
        else:
            print(f"Number of employees in {originalCounty}: {employeeCount}")
    
    
    def viewCountEmployeePerEmailProvider(self):
        # Display Available Email Providers
        emailProviders = self.model.getEmailProviers()
        print("Available Email Providers: ")
        for emailProvider in emailProviders:
            print(emailProvider, end = ", ")
        print()
        
        # Input Email Provider
        inputEmailProvider = inputComparator("Enter Email Provider: ", "Please Enter a valid Email Provider", comparator = notblank)
        print()
        
        # Call Model
        modelData = self.model.countEmployeeEmailProvider(inputEmailProvider)
        employeeCount = modelData["Count"]
        originalEmailProvider = modelData["EmailProvider"]
        
        # Bind Model To UI
        if employeeCount == 0:
            print(f"There are no employees using {originalEmailProvider} as Email Provder")
        else:
            print(f"Number of employees using '{originalEmailProvider}' as Email Provider: {employeeCount}")
    