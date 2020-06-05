from src.entities.Employee.Employee import *
from src.entities.Employee.PayrollRecord import *

class EntityManager:
    def __init__(self, employees, payrolls, departments, positions):
        self.employees = employees
        self.payrollRecords = payrolls
        self.departments = departments
        self.positions = positions
        
    def saveState(self):
        self.employees.saveState()
        self.payrollRecords.saveState()
    
    def retrieveState(self):
        self.employees.retrieveState()
        self.payrollRecords.retrieveState()

class EntityManagerFactory:
    def create(self):
        departments = {
            "Accounting" : Accounting(),
            "Human Resources" : HumanResources(),
            "Sales" : Sales(),
            "Marketing" : Marketing(),
            "Manufacturing" : Manufacturing(),
            "Admin" : Admin(),
        }
        
        positions = {
            "Manager" : Manager,
            "Assistant Manager" : AssistantManager,
            "Secretary" : Secretary,
            "Staff" : Staff,
        }
        
        factory = FileBoundEmployeesFactory(departments, positions)
        employees = factory.create()
        payrollfactory = FileBoundPayrollsEntityFactory()
        payrollRecords = payrollfactory.create(employees)
        return EntityManager(employees, payrollRecords, departments, positions)
    