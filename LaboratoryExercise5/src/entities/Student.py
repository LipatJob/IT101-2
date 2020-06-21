from lib.FileBound import FileBound
from lib.filestrategy.JsonStrategy import JsonDecoder, JsonEncoder
from lib.FileDataHandler import FileDataHandler
import os

# Data classes
class Student:
    def __init__(self, studentNo = "", lastName = "", firstName = "", 
                 gender = None, description = "", program = "", interests = {}):
        self.studentNo = studentNo
        self.lastName = lastName
        self.firstName = firstName
        self.gender = gender
        self.description = description
        self.program = program
        self.interests = interests
        
        # Default Value
        if len(interests) == 0:
           self.interests = {
                "Sports"        : False,
                "Music"         : False,
                "Arts"          : False,
                "Science"       : False,
                "Technology"    : False,
                "Nature"        : False
            }
    
    def toSerializable(self):
        data = {
            "StudentNo"     : self.studentNo,
            "LastName"      : self.lastName,
            "FirstName"     : self.firstName,
            "Gender"        : self.gender,
            "Description"   : self.description,
            "Program"       : self.program,
            "Interests"     : self.interests
        }
        return data

class Students:
    programs = ["BSIT", "BS", "BSCS", "BSIS", "BSBA", "BSCPE", "BSN", "BSECE", "BSEE", "BSARCHI", "BSCHE", "BSIE"]
    
    def __init__(self):
        self.students = {}
        
    def addStudent(self, entity):
        self.students[entity.studentNo] = entity
        
    def deleteStudent(self, entity):
        del self.students[entity.studentNo]
    
    def getStudent(self, entity):
        return self.students[entity.studentNo]
    
    def updateStudent(self, entity):
        self.deleteStudent(entity.studentNo)
        self.addStudent(entity)
        
    def getPrograms(self):
        return Students.programs
    
    def doesStudentNumberExist(self, studentNumber):
        return studentNumber in self.students

# Filebound

class FileBoundStudents(Students, FileBound):
    def __init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy):
        Students.__init__(self)
        FileBound.__init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy)
        
    def toSerializable(self):
        data = []
        for student in self.students.values():
            data.append(student.toSerializable())
        return data
    
    def setData(self, data):
        self.students = {}
        for student in data:
            self.addStudent(Student(
                studentNo = student["StudentNo"], lastName = student["LastName"], 
                firstName = student["FirstName"], gender = student["Gender"], 
                description = student["Description"], program = student["Program"], 
                interests = student["Interests"]))

# Factory

class FileBoundStudentsFactory():
    def create(self):
        encoder = JsonEncoder()
        decoder = JsonDecoder()
        cwd = os.getcwd()
        fileHandler = FileDataHandler(cwd + "\\data\\metadata.json")
        return FileBoundStudents(fileHandler, decoder, encoder)
 
    

