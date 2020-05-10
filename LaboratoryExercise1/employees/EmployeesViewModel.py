from datetime import datetime
from dateutil.relativedelta import relativedelta

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
            age = relativedelta(datetime.now(), employee["bdate"]).years
            if age <= end and age >= start:
                employee["age"] = age
                employees.append(employee)
        return {"Employees": employees}
    
    def filterEmployeeCity(self, city):
        employees = []
        if city in self._entity.cities:
            for employeeKey in self._entity.cities[city]:
                employees.append(self._entity.employees[employeeKey])
        return {"Employees": employees}
    
    def countEmployeeCounty(self, county):
        count = 0
        if county in self._entity.counties:
            count = len(self._entity.counties[county])
        return {"Count": count}
    
    def countEmployeeEmailProvider(self, emailProvider):
        count = 0
        if emailProvider in self._entity.emailProviders:
            count = len(self._entity.emailProviders[emailProvider])
        return {"Count": count}
    
    def getCounties(self):
        return self._entity.counties.keys()
    
    def getCities(self):
        return self._entity.cities.keys()

    def getEmailProviers(self):
        return self._entity.emailProviders.keys()