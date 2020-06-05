class Department:
    def __init__(self, name):
        self.name = name
        self.positions = {
            "Manager" : None,
            "Assistant Manager" : None,
            "Secretary" : None,
            "Staff" : []
        }
    
        
    def setManager(self, employee):
        self.positions["Manager"] = employee
    
    
    def setAssistantManager(self, employee):
        self.positions["Assistant Manager"] = employee
        
        
    def setSecretary(self, employee):
        self.positions["Secretary"] = employee
        
        
    def addStaff(self, employee):
        self.positions["Staff"].append(employee)
        
        
    def isPositionAvaiable(self, position):
        if position == "Staff":
            return True
        return self.positions[position] == None

        
    def addEmployeeToPosition(self, position, employee):
        self.positions[position] = employee

    
    def getAvailablePositions(self):
        available = {"Staff"}
        for position, employee in self.positions.items():
            if employee == None:
                available.add(position)
        return available
    
    def removeEmployee(self, employeeNumber):
        for index, employee in self.positions["Staff"]:
            if employee.employeeNumber == employeeNumber:
                del self.positions["Staff"][index]   
                     
        for position, employee in self.positions.items():
            if position == "Staff":
                continue
            if employee != None and employee.employeeNumber == employeeNumber:
                self.positions[position] = None
        
            


class Accounting(Department):
    def __init__(self):
        super().__init__("Accounting")


class HumanResources(Department):
    def __init__(self):
        super().__init__("Human Resources")

        
class Sales(Department):
    def __init__(self):
        super().__init__("Sales")

        
class Marketing(Department):
    def __init__(self):
        super().__init__("Marketing")


class Manufacturing(Department):
    def __init__(self):
        super().__init__("Manufacturing")

        
class Admin(Department):
    def __init__(self):
        super().__init__("Admin")

