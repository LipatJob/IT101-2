from datetime import datetime
from lib.CaseInsensitiveDict import CaseInsensitiveDict

class CitiesViewModel:
    """ Queries entities to be used in ControllerView """
    def __init__(self, entity, cityFactory):
        self._entity = entity
        self.cityFactory = cityFactory
        
        
    def getCityNames(self):
        return {city.cityName for city in self._entity.getCities()}
    
    def doesCityExist(self, city):
        cities = self.getCaseInsensitiveCityNames()
        return city in cities
    
    def getCaseInsensitiveCityNames(self):
        cities = CaseInsensitiveDict()
        for city in self._entity.getCities():
            cityName = city.cityName.lower()
            cities[cityName] = cityName
        return cities
    
    def getOriginalCityNameCase(self, cityName):
        for city in self._entity.getCities():
            if city.cityName.lower() == cityName:
                return city.cityName 
        return cityName
    
    def getCityCount(self):
        return len(self._entity.getCities())
    
    def getCity(self, cityName):
        return self._entity.getCity(cityName)
    
    
    def addCity(self, cityName):
        fileName = cityName.replace(" ","") + "Case.txt"
        city = self.cityFactory.create(cityName, fileName)
        city.saveState()
        self._entity.addCity(city)
        self._entity.saveState()

    def getCaseInsensitiveBarangayNames(self, cityName):
        city = self._entity.getCity(cityName)
        barangayNames = CaseInsensitiveDict()
        
        for barangayName in city.getBarangays():
            barangayNames[barangayName] = barangayName
            
        return barangayNames 
    
    
    def addBarangay(self, cityName, barangayName):
        city = self.getCity(cityName)
        barangay = self.getDefaultBarangay(barangayName)
        city.addBarangay(barangay)
        city.saveState()
    
    
    def deleteBarangay(self, cityName, barangayName):
        city = self.getCity(cityName)
        city.deleteBarangay(barangayName)
        city.saveState()
    
    
    def editBarangay(self,cityName, barangayName, data):
        city = self.getCity(cityName)
        city.editBarangay(barangayName, data)
        city.saveState()
        
    def getBarangays(self, cityName):
        city = self.getCity(cityName)
        return city.getBarangays()
    
    def getDefaultBarangay(self, barangayName):
        val = (
                barangayName, {
                    "Confirmed" : 0,
                    "Active" : 0,
                    "Recovered" : 0,
                    "Suspect" : 0,
                    "Probable" : 0,
                    "Deceased" : 0
                }
        )
        return val
        
        
        
        
    
        
















    def getEmployeeList(self):
        return self._entity.employees.getAllEmployees()


    def getEmployee(self, id):
        return self._entity.employees.getEmployee(id)
    
    
    def addEmployee(self, employee):
        self._entity.employees.addEmployee(employee)
        self._entity.saveState()


    def getMonthOfEmployeeRecords(self, employeeNumber):
        months = set()
        for record in self._entity.payrollRecords.getAllRecords():
            if record.employee.employeeNumber == employeeNumber:
                months.add(record.month)
        return months
            
            
    def addPayrollRecord(self, payrollRecord):
        self._entity.payrollRecords.addRecord(payrollRecord)
        self._entity.saveState()


    def generatePayrollRecord(self, employeeNumber, month):
        currentRecord = self._entity.payrollRecords.getRecord(employeeNumber, month)
        employee = currentRecord.employee
        
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        
        # Build ViewModel
        recordView                  = PayrollRecordEntityView()
        recordView.month            = months[currentRecord.month]
        recordView.employeeNumber   = employee.employeeNumber
        recordView.employeeName     = employee.lastName + ", " + employee.firstName
        recordView.department       = employee.department
        recordView.ratePerDay       = employee.ratePerHour * 8
        recordView.daysWorked       = currentRecord.daysWorked
        recordView.grossPay         = recordView.ratePerDay * currentRecord.daysWorked
        
        return recordView
        
    
    def getDepartments(self):
        departments = CaseInsensitiveDict()
        originalDepartments = {"Accounting", "Marketing", "Human Resources", "Finance", "MIS", "Admin"}
        for department in originalDepartments:
            departments[department] = department
        return departments
    
        
    def getEmployeeNumbers(self):
        return {employee.employeeNumber for employee in self._entity.employees.getAllEmployees()}
    
    def getRecordEmployeeNumbers(self):
        return {record.employee.employeeNumber for record in self._entity.payrollRecords.getAllRecords()}
    
    def getRecordEmployeeNumbersForMonth(self, month):
        employeeNumbers = set()
        
        for record in self._entity.payrollRecords.getAllRecords():
            if record.month == month:
                employeeNumbers.add(record.employee.employeeNumber)
        
        return employeeNumbers
        

    
    
    