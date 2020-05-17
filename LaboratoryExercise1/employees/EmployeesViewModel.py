from datetime import datetime

class EmployeesViewModel:
    def __init__(self, employeesEntityManager):
        self._entity = employeesEntityManager
    
    def employeeCount(self):
        employeeCount = len(self._entity.employees)
        return {"EmployeeCount" : employeeCount}
    
    def filterEmployeeAgeRange(self, start, end):
        employees = []
        for employee in self._entity.employees.values():
            # get years difference
            age = self._getAge(datetime.now(), employee["bdate"])
            if age <= end and age >= start:
                employee["age"] = age
                employees.append(employee)
        return {"Employees" : employees}
    
    def filterEmployeeCity(self, city):
        employees = []
        originalCity = city
        if city in self._entity.cities:
            originalCity = self._getOriginalValue(self._entity.cities, city)
            for employeeKey in self._entity.cities[city]:
                employees.append(self._entity.employees[employeeKey])
                
        return {"Employees" : employees, "City" : originalCity}
    
    def countEmployeeCounty(self, county):
        count = 0
        originalCounty = county
        if county in self._entity.counties:
            originalCounty = self._getOriginalValue(self._entity.counties, county)
            count = len(self._entity.counties[county])
        return {"Count" : count, "County" : originalCounty}
    
    def countEmployeeEmailProvider(self, emailProvider):
        count = 0
        originalEmailProvider = emailProvider
        if emailProvider in self._entity.emailProviders:
            originalEmailProvider = self._getOriginalValue(self._entity.emailProviders, emailProvider)
            count = len(self._entity.emailProviders[emailProvider])
        return {"Count" : count, "EmailProvider" : originalEmailProvider}
    
    def getCounties(self):
        return self._entity.counties.keys()
    
    def getCities(self):
        return self._entity.cities.keys()

    def getEmailProviers(self):
        return self._entity.emailProviders.keys()
    
    def _getOriginalValue(self, dictionary, value):
        """ Retrieves the original value in a case insensitive dictionary
         
         Example:
         nocasedict = {"Hello World", "Python", "MCL"}
         print(_getRetrievedValue(noCaseDict, "mcl")) # Input: 'mcl' -> output: 'MCL' (because MCL is in nocasedict not mcl)
        """
        originalCase = {key.lower() : key for key in dictionary.keys()}
        return originalCase[value.lower()]
    
    def _getAge(self, currentDate, birthDate):
        age = currentDate.year - birthDate.year - 1
        
        if currentDate.month > birthDate.month:
            age += 1
            
        if currentDate.month == birthDate.month and currentDate.day >= birthDate.day:
            age += 1
            
        return age
        
        
    