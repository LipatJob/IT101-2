from src.entities.Student import *
class Model:
    def __init__(self, students):
        self.students = students
        
    def saveStudent(self, entity):
        self.students.addStudent(entity)
        self.students.saveState()
        
    def getStudent(self, entity):
        return self.students.getStudent(entity)


    def getBlankEntity(self):
        return Student()


    def deleteStudent(self, entity):
        self.students.deleteStudent(entity)
        self.students.saveState()


    def studentNumberExists(self, studentNumber):
        return self.students.doesStudentNumberExist(studentNumber)


    def buildEntity(self, studentNo = "", lastName = "", firstName = "", 
                 gender = None, description = "", program = "", interests = {}):
        return Student(studentNo, lastName, firstName, gender, description, program, interests)


    def getProgramIndex(self, fprogram):
        for index, program in enumerate(self.students.getPrograms()):
            if program == fprogram: return index
        return None


    def getProgramList(self):
        return self.students.getPrograms()

