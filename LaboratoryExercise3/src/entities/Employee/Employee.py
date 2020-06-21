from abc import ABC, abstractmethod
from src.entities.Employee.Department import *
from lib.FileBound import FileBound
from lib.filestrategy.FileEncoder import FileEncoder
from lib.filestrategy.FileDecoder import FileDecoder
from lib.FileDataHandler import FileDataHandler
from datetime import datetime
import os




""" Entities """
class Employee:
    def __init__(self, employeeNumber = "", lastName = "", firstName = "", 
                 position = "", department = None, birthdate = None, ratePerDay = 0, allowance = 0):
        self.employeeNumber = employeeNumber
        self.lastName = lastName
        self.firstName = firstName
        self.position = position
        self.department = department
        self.birthdate = birthdate
        self.ratePerDay = ratePerDay
        self.allowance = allowance
        self.startSalary = 0
        self.startAllowance = 0
        self._initDepartment()
    
    @abstractmethod
    def _initDepartment(self):
        pass        
    
    def increasePay(self):
        self.ratePerDay += self.ratePerDay * .5
        
    def setStartRate(self):
        self.ratePerDay = self.startRate
        
    def setStartAllowance(self):
        self.allowance = self.startAllowance


        
class Manager(Employee):
    def _initDepartment(self):
        self.department.setManager(self)
        self.startRate = 1000
        self.startAllowance = 5000
    
    def increasePay(self):
        self.ratePerDay += self.ratePerDay
        
    

        
class AssistantManager(Employee):
    def _initDepartment(self):
        self.department.setAssistantManager(self)
        self.startRate = 750
        self.startAllowance = 3000
        
    def increasePay(self):
        self.ratePerDay += self.ratePerDay



class Secretary(Employee):
    def _initDepartment(self):
        self.department.setSecretary(self)
        self.startRate = 500



class Staff(Employee):
    def _initDepartment(self):
        self.department.addStaff(self)
        self.startRate = 475
        

class Employees:
    def __init__(self):
        self.employees = dict()
    

    def addEmployee(self, employee):
        self.employees[employee.employeeNumber] = employee
    

    def getEmployee(self, id):
        return self.employees[id]
    

    def getAllEmployees(self):
        return self.employees.values()
    

    def resetEmployees(self):
        self.employees = {}
        
        
    def deleteEmployee(self, id):
        del self.employees[id]

    
    def getEmployee(self, employeeNumber):
        for employee in self.employees.values():
            if employee.employeeNumber == employeeNumber:
                return employee
        return None
        
        
""" Behavioral Classes """
class EmployeeFactory:
    def __init__(self, departments, positions):
        self.departments = departments
        self.positions = positions
    
    def create(self, employeeNumber = "", lastName = "", firstName = "", 
                 position = "", department = "", birthdate = "", ratePerDay = 0, allowance = 0):
        tempDepartment = self.departments[department]
        tempDate = datetime.strptime(birthdate,'%m-%d-%Y')
        tempPosition = self.positions[position]
        
        return tempPosition(employeeNumber, lastName, firstName, position, tempDepartment, birthdate, ratePerDay, allowance)


class FileBoundEmployeesFactory:
    def __init__(self, departments, positions):
        self.departments = departments
        self.positions = positions
    
    def create(self):
        cwd = os.getcwd()
        employeeEncoder = FileEncoder(",",";\n")
        employeeDecoder = FileDecoder(",",";")
        employeeFileHandler = FileDataHandler(cwd + "\\data\\empList.txt")
        factory = EmployeeFactory(self.departments, self.positions)
        return FileBoundEmployees(employeeFileHandler, employeeDecoder, employeeEncoder, factory)
    
    
class FileBoundEmployees(Employees, FileBound):
    def __init__(self,fileHandler, dataParsingStrategy, dataEncodingStrategy, factory):
        Employees.__init__(self)
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
        self.factory = factory
        
    def toSerializable(self):
        """ Convert data into array """
        arr = []
        for val in self.employees.values():
            tempArr = []
            tempArr.append(str(val.employeeNumber))
            tempArr.append(str(val.lastName))
            tempArr.append(str(val.firstName))
            tempArr.append(str(val.position))
            tempArr.append(str(val.department.name))
            tempArr.append(str(val.birthdate))
            tempArr.append(str(val.ratePerDay))
            tempArr.append(str(val.allowance))
            
            arr.append(tempArr)
        return arr  
    
    
    def setData(self, data):
        """ Set data from array """
        for row in data:
            if len(row) == 1:
                continue
            # row[0] = id, row[1] = lastname, row[2] = firstname, row[3] = position, 
            # row[4] = department, row[5] = birthdate, row[6] = ratePerDay
            employee = self.factory.create(
                    employeeNumber = row[0], lastName = row[1], firstName = row[2], position = row[3], 
                    department = row[4], birthdate = row[5], ratePerDay = float(row[6]), allowance = float(row[7])
                    )
            self.addEmployee(employee)
