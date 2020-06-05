from lib.Helper import inputComparator, inputNumber, notblank, isNumber, isWhole, multipleValidation, printAsTable, isAlphaOrSpace
from cases.CitiesViewModel import CitiesViewModel

class CitiesViewController:
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
    def __init__(self, model : CitiesViewModel):
        self.model = model
    
    
    def viewMenu(self, response = ""):
        menu =(
        "--------------------------------------------------------\n"\
        "       MCL-CCIS COVID-19 Case Tracker Admin Panel\n"\
        "--------------------------------------------------------\n"\
        "Value\tAction\n"\
        "-----\t------\n"\
        "  A\tSelect Tracked City\n"\
        "  B\tAdd City to Track\n"\
        "  X\tExit\n"\
        "--------------------------------------------------------"
        )
        
        print(menu)
        if response != None and response != "":
            print(">",response)
        
        selectionItems = {
            "a" : self.selectCity,
            "b" : self.createCasesForCity,
            "x" : exit
        }
        

        selection = selectionItems[inputComparator(message = "Please Enter One of the Values: ", 
                                                   errorMessage = "Please select one of the values.", 
                                                   comparator = multipleValidation((lambda x: x in selectionItems)), 
                                                   force_lower = True, strip = True)]
        response = selection()
        print()
        self.viewMenu(response)
        print()
        
        
    def selectCity(self):
        # If there are no cities
        if not self._cityCountMoreThanZero:
            print("There are No Tracked Cities")
            return
        
        # Display Available Cities
        cityNames = sorted(list(self.model.getCityNames()))
        print("Available Cities: ")
        for cityName in cityNames:
            print(cityName)
        
        city = inputComparator(message = "Enter City Name: ", 
                               errorMessage = "Please select one of the values.", 
                               comparator = multipleValidation(self._validateSelectCity), 
                               force_lower = True, strip = True)
        
        city = self.model.getOriginalCityNameCase(city)
        self.viewCity(city)
        
        
    def viewCity(self, selectedCity, response = ""):
        menu = (
        f"--------------------------------------------------------\n"\
        f"       MCL-CCIS COVID-19 Case Tracker Admin Panel\n"\
        f"--------------------------------------------------------\n"\
        f"Value\tAction\n"\
        f"-----\t------\n"\
        f"  A\tView Cases for City\n"\
        f"  B\tEdit Cases for City\n"\
        f"  C\tAdd Barangay\n"\
        f"  D\tDelete Barangay\n"\
        f"  X\tBack\n"\
        f"\n"
        f"Selected City: {selectedCity}\n"\
        f"--------------------------------------------------------"
        )
        print(menu)
        if response != None and response != "":
            print(">",response)
        
        selectionItems = {
            "a" : self.viewCasesForCity,
            "b" : self.editCasesForCity,
            "c" : self.addBarangay,
            "d" : self.deleteBarangay,
            "x" : "x",
        }
        
        selection = inputComparator(message = "Please Enter One of the Values: ", 
                                    errorMessage = "Please select one of the values.", 
                                    comparator = (lambda x: x in selectionItems), 
                                    force_lower = True, strip = True)
        if selection == "x":
            return
        
        response = selectionItems[selection](selectedCity)
        print()
        self.viewCity(selectedCity, response)
        print()
        
        
    def viewCasesForCity(self, cityName):
        city = self.model.getCity(cityName)
        barangay = city.barangays.items()
        if len(barangay) == 0:
            return f"There are No Tracked Barangays For {cityName}"
        
        print(f"Cases for {cityName}")
        data = [['BARANGAY', 'CONFIRMED', 'ACTIVE', 'RECOVERED', 'SUSPECT', 'PROBABLE', 'DECEASED']]
        for barangayName, barangayData in barangay:
            brgyRow = []
            brgyRow.append(barangayName)
            brgyRow.append(barangayData["Confirmed"])
            brgyRow.append(barangayData["Active"])
            brgyRow.append(barangayData["Recovered"])
            brgyRow.append(barangayData["Suspect"])
            brgyRow.append(barangayData["Probable"])
            brgyRow.append(barangayData["Deceased"])
            data.append(brgyRow)
        data[1:] = sorted(data[1:], key = lambda val: val[1], reverse = True)
        printAsTable(data)


    def editCasesForCity(self, cityName):
        city = self.model.getCity(cityName)
        # Display Available Barangays
        barangays = self.model.getBarangays(cityName)
        
        if len(barangays) == 0:
            return f"There are No Tracked Barangays for {cityName}"
            
        
        for barangay in barangays:
            print(barangay)
        
        # Input Barangay Name
        barangayName = inputComparator(message = "Enter Barangay Name: ", 
                            errorMessage = "Please Enter a Valid Barangay Name.", 
                            comparator = multipleValidation(self._validateBarangayExists(cityName)),
                            force_lower = True, strip = True)
        barangayName = self.model.getCaseInsensitiveBarangayNames(cityName)[barangayName]
        barangay = dict(city.getBarangay(barangayName))
        
        # Display Details of Barangay
        print(
            f"Select Field to Edit\n"
            f"A. Active: {barangay['Active']}\n"
            f"B. Recovered: {barangay['Recovered']}\n"
            f"C. Suspect: {barangay['Suspect']}\n"
            f"D. Probable: {barangay['Probable']}\n"
            f"E. Deceased: {barangay['Deceased']}\n"
            f"X. Back"
        )
        
        selection = {"a" : "Active",
                     "b" : "Recovered",
                     "c" : "Suspect",
                     "d" : "Probable",
                     "e" : "Deceased",
                     "x" : "x"}
        editSelection = inputComparator(message = "Please Select One of the Values: ", 
                            errorMessage = "Please Enter a Valid Value.", 
                            comparator = multipleValidation(lambda val: val in selection), 
                            force_lower = True, strip = True)
        
        if editSelection == "x": # Go back
            return
       
        newBarangay = self.editBarangayCaseValue(cityName, barangayName, selection[editSelection])
        self.model.editBarangay(cityName,barangayName, newBarangay)     
        # Input Value
        print("Successfully Edited Barangay Values")
        
        if input("Enter 'Y' to Edit Another Barangay:").lower() == "y":
            self.editCasesForCity(cityName)
    
    
    def editBarangayCaseValue(self, cityName, barangayName, field):
        city = self.model.getCity(cityName)
        barangay = dict(city.getBarangay(barangayName))
        
        def negativeToZero(val):
            return 0 if val < 0 else val
        
        if field == "Barangay Name":
            pass
        elif field == "Active":
            # Display Current value
            print("Current Value of Active:",barangay["Active"])
                        
            # Update Value
            barangay["Active"] = inputNumber(message = "Please Enter New Value: ", 
                            errorMessage = "Please Enter a Valid Value.", 
                            comparator = multipleValidation(lambda val: val >= 0))
            
            # Change other values
            barangay["Confirmed"] = barangay["Active"] + barangay["Recovered"] + barangay["Deceased"]
            
        elif field == "Recovered":
            # Display Current value
            print("Current Value of Recovered:",barangay["Recovered"])
            
            # Update Value
            barangay["Recovered"] = inputNumber(message = "Please Enter New Value: ", 
                            errorMessage = "Please Enter a Valid Value.", 
                            comparator = multipleValidation(lambda val: val >= 0))
            
            # Ask User if Adjust Active Cases
            if input("Enter `Y to Adjust Active Cases: ").lower() == "y":
                barangay["Active"] = negativeToZero(barangay["Confirmed"] - (barangay["Recovered"] + barangay["Deceased"]))
                print("Active Cases Adjusted")
                
            # Change other values
            barangay["Confirmed"] = barangay["Active"] + barangay["Recovered"] + barangay["Deceased"]
            
        elif field == "Suspect":
            # Display Current value
            print("Current Value of Suspect:",barangay["Suspect"])
            
            # Update Value
            barangay["Suspect"] = inputNumber(message = "Please Enter New Value: ", 
                            errorMessage = "Please Enter a Valid Value.", 
                            comparator = multipleValidation(lambda val: val >= 0))
            
        elif field == "Probable":
            # Display Current value
            print("Current Value of Probable:",barangay["Probable"])
            
            # Update Value
            barangay["Probable"] = inputNumber(message = "Please Enter New Value: ", 
                            errorMessage = "Please Enter a Valid Value.", 
                            comparator = multipleValidation(lambda val: val >= 0))
            
        elif field == "Deceased":
            # Display Current value
            print("Current Value of Deceased:",barangay["Deceased"])
            
            # Update Value
            barangay["Deceased"] = inputNumber(message = "Please Enter New Value: ", 
                            errorMessage = "Please Enter a Valid Value.", 
                            comparator = multipleValidation(lambda val: val >= 0))
            
            # Ask user if Adjust Active Case
            if input("Enter `Y to Adjust Active Cases: ").lower() == "y":
                barangay["Active"] = negativeToZero(barangay["Confirmed"] - (barangay["Recovered"] + barangay["Deceased"]))
                print("Active Cases Adjusted")
                
            # Change other values
            barangay["Confirmed"] = barangay["Active"] + barangay["Recovered"] + barangay["Deceased"]
        return barangay
    

    def addBarangay(self, cityName):
        barangayName = inputComparator(message = "Enter Barangay Name to Add: ", 
                            errorMessage = "Please Enter a Valid Barangay Name.", 
                            comparator = multipleValidation(self._validateAddBarangay(cityName)), 
                            force_lower = False, strip = True).upper()
        self.model.addBarangay(cityName, barangayName)
        return "Barangay Successfully Added"
    

    def deleteBarangay(self, cityName):
        barangays = self.model.getBarangays(cityName)

        if len(barangays) == 0:
            return f"There are No Tracked Barangays for {cityName}"
            
        
        # Display Available Barangays
        for barangay in barangays:
            print(barangay)
        
        # Input Barangay Name
        barangayName = inputComparator(message = "Enter Barangay Name to Delete: ", 
                            errorMessage = "Please Enter a Valid Barangay Name.", 
                            comparator = multipleValidation(self._validateDeleteBarangay(cityName)), 
                            force_lower = False, strip = True)
        barangayName = self.model.getCaseInsensitiveBarangayNames(cityName)[barangayName]
        
        # Delete Barangay
        self.model.deleteBarangay(cityName, barangayName)
        return "Barangay Successfully Removed"


    def createCasesForCity(self):
        cityNames = self.model.getCityNames()
        print("Existing Cities: ")
        for cityName in cityNames:
            print(cityName)
        city = inputComparator(message = "Enter City Name to Add: ", 
                               errorMessage = "Please Enter a Valid City Name.", 
                               comparator = multipleValidation(self._validateCreateCasesForCity), 
                               force_lower = False, strip = True).title()
        self.model.addCity(city)
        return "City Successfully Added"
    
    
    
    # VALIDATION
    
    
    def _cityCountMoreThanZero(self, val):
        return self.model.getCityCount() > 0
    
    
    def _validateSelectCity(self, city):
        if not self.model.doesCityExist(city):
            print("Please Enter an Existing City")
            return False
        return True
    
    
    def _validateCreateCasesForCity(self, val):
        # City is not blank
        if not self._validateCityName(val):
            return False
        # City does not exist
        if self._cityNameExists(val):
            print("City Already Exists")
            return False
        return True
    
    def _validateCityName(self, val):
        if len(val) == 0:
            return False
        if val.isspace():
            return False
        for letter in val:
            if not (letter.isalpha() or letter == " " or letter == "."):
                return False
        return True
    
    def _validateAddBarangay(self, cityName):
        barangays = self.model.getCaseInsensitiveBarangayNames(cityName)
        def validate(barangayName):
            if barangayName in barangays:
                print("Barangay Already Exists")
                return False
            if len(barangayName.strip()) == 0:
                return False
            return True
        return validate
    
    
    def _validateDeleteBarangay(self, cityName):
        barangays = self.model.getCaseInsensitiveBarangayNames(cityName)
        def validate(barangayName):
            if barangayName not in barangays:
                print("Barangay Doesn't Exist")
                return False
            return True
        return validate
    
    def _validateBarangayExists(self, cityName):
        barangays = self.model.getCaseInsensitiveBarangayNames(cityName)
        def validate(barangayName):
            if barangayName not in barangays:
                print("Barangay Doesn't Exist")
                return False
            return True
        return validate
    

    def _cityNameExists(self, cityName):
        cityNames = self.model.getCaseInsensitiveCityNames()
        return cityName in cityNames
    
    def _barangayNameExists(self, cityName):
        cityNames = self.model.getCaseInsensitiveCityNames()
        return cityName in cityNames
    
    