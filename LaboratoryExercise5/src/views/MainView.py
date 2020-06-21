from tkinter import *
from tkinter import messagebox
from lib.ValidatedWidgets import *
from lib.Helper import *

class MainView(Frame):
    def __init__(self, master = None, model = None):
        super().__init__(master=master)
        
        self.model = model
        
        self.initializeWidgets()
        self.pack()

    
    def initializeWidgets(self):
        titleFont = "Verdana 12 bold"
        self.mainFont = "Verdana 9 bold"
        self.inputFont = "Verdana 9"
        titleLabel = Label(self, text = "Student Information", font = titleFont)
        titleLabel.grid(row = 0, column = 0)
        
        self.initializeInfoGroup1()
        self.initalizeInfoGroup2()
        self.initializeButtonGroup()
    

    def initializeInfoGroup1(self):
        # INFO GROUP 1: Student No, Last Name, First Name, Gender
        infoGroup1 = Frame(self, pady = 10)
        infoGroup1.grid(row = 1, column = 0)
        
        textFrame = Frame(infoGroup1)
        # Row 0
        studentNoLabel = Label(textFrame, text = "Student No.", font = self.mainFont)
        self.studentNoEntry = ValidatedEntry(textFrame, font =  self.inputFont, validation = self.validateStudentNumber)
        self.searchBtn = Button(textFrame, text = "Search", font = self.mainFont, command = self.searchAction)

        studentNoLabel.grid(row = 0, column = 1)
        self.studentNoEntry.grid(row = 0, column = 2)
        self.searchBtn.grid(row = 0, column = 3)
        
        # Row 1
        lastNameLabel = Label(textFrame, text = "Last Name", font = self.mainFont)
        self.lastNameEntry = ValidatedEntry(textFrame, font = self.inputFont, validation = self.validateLastName)
        
        lastNameLabel.grid(row = 1, column = 1)
        self.lastNameEntry.grid(row = 1, column = 2)
        
        firstNameLabel = Label(textFrame, text = "First Name", font = self.mainFont)
        self.firstNameEntry = ValidatedEntry(textFrame, font =  self.inputFont, validation = self.validateFirstName)
        
        firstNameLabel.grid(row = 1, column = 4)
        self.firstNameEntry.grid(row = 1, column = 5)
        
        textFrame.pack(side = TOP, anchor = W, expand = YES)
        
        # Row 2
        self.selectedGender = ValidatedStringVar(validation = self.validateGender)
        self.selectedGender.set(None)
        radioFrame = Frame(infoGroup1)
        genderLabel = Label(radioFrame, text = "Gender", font = self.mainFont)
        self.maleRadio = Radiobutton(radioFrame, text = "Male", font = self.mainFont, variable = self.selectedGender, value = "Male")
        self.femaleRadio = Radiobutton(radioFrame, text = "Female", font = self.mainFont, variable = self.selectedGender, value = "Female")
        
        radioFrame.pack(side = TOP, anchor = W, expand = YES)
        genderLabel.grid(row = 0, column = 1)
        self.maleRadio.grid(row = 0, column = 2)
        self.femaleRadio.grid(row = 0, column = 3)
        
        
    def initalizeInfoGroup2(self):
        infoGroup2 = Frame(self)
        infoGroup2.grid(row = 2, column = 0)
        
        # Column 1
        # Row 0
        column1 = Frame(infoGroup2, padx = 10, pady = 5)
        descriptionLabel = Label(column1, text = "Description", font = self.mainFont)
        self.descriptionText = Text(column1, height = 10, width = 25, font = self.inputFont)
        
        column1.grid(row = 0, column = 0, sticky = "N")
        descriptionLabel.grid(row = 0, column = 0, sticky = "W")
        self.descriptionText.grid(row = 1, column = 0)
        
        # Column 2
        column2 = Frame(infoGroup2, padx = 10, pady = 5)
        interestLabel = Label(column2, text = "Choose Interest", font = self.mainFont)
        
        column2.grid(row = 0, column = 1, sticky = "N")
        interestLabel.grid(row = 0, column = 0)
        
        self.sportsCheckValue = BooleanVar(value = False)
        self.musicCheckValue = BooleanVar(value = False)
        self.artsCheckValue = BooleanVar(value = False)
        self.scienceCheckValue = BooleanVar(value = False)
        self.technologyCheckValue = BooleanVar(value = False)
        self.natureCheckValue = BooleanVar(value = False)
        
        sportsCheck = Checkbutton(column2, text = "Sports", font = self.mainFont, variable = self.sportsCheckValue)
        musicCheck = Checkbutton(column2, text = "Music", font = self.mainFont, variable = self.musicCheckValue)
        artsCheck = Checkbutton(column2, text = "Arts", font = self.mainFont, variable = self.artsCheckValue)
        scienceCheck = Checkbutton(column2, text = "Science", font = self.mainFont, variable = self.scienceCheckValue)
        technologyCheck = Checkbutton(column2, text = "Technology", font = self.mainFont, variable = self.technologyCheckValue)
        natureCheck = Checkbutton(column2, text = "Nature", font = self.mainFont, variable = self.natureCheckValue)
        
        sportsCheck.grid(row = 1, column = 0, sticky = "W")
        musicCheck.grid(row = 2, column = 0, sticky = "W")
        artsCheck.grid(row = 3, column = 0, sticky = "W")
        scienceCheck.grid(row = 4, column = 0, sticky = "W")
        technologyCheck.grid(row = 5, column = 0, sticky = "W")
        natureCheck.grid(row = 6, column = 0, sticky = "W")
        
        
        # Column 3
        column3 = Frame(infoGroup2, padx = 10, pady = 5)
        column3.grid(row = 0, column = 2, sticky = "N")
        
        programLabel = Label(column3, text = "Select Program", font = self.mainFont)
        programScrollFrame = Frame(column3)
        programScrollBar = Scrollbar(programScrollFrame)
        self.programListbox = ValidatedListBox(programScrollFrame, font = self.mainFont, validation = self.validateProgram)
        
        ## Setup Scroll Bar
        programScrollBar.config(command = self.programListbox.yview)                
        self.programListbox.config(yscrollcommand = programScrollBar.set)   
        
        ## Setup List
        programItems = self.model.getProgramList()
        for item in programItems: self.programListbox.insert(END, item)
        
        programLabel.grid(row = 0, column = 0)
        programScrollFrame.grid(row = 1, column = 0)
        programScrollBar.pack(side=RIGHT, fill=Y)
        self.programListbox.pack(side=LEFT, expand=YES, fill=BOTH)
        
        
    def initializeButtonGroup(self):
        actionGroup = Frame(self, pady = 10, padx = 40)
        actionGroup.grid(row = 3, column = 0, sticky = "E")
        
        self.deleteButton = Button(actionGroup, text = "Delete", font = self.mainFont, command = self.deleteAction)
        self.newButton = Button(actionGroup, text = "New", font = self.mainFont, command = self.newAction)
        self.saveButton = Button(actionGroup, text = "Save", font = self.mainFont, command = self.saveAction)
        
        self.deleteButton.pack(side = LEFT)
        self.newButton.pack(side = LEFT)
        self.saveButton.pack(side = LEFT)
    
    
    
    ## ACTIONS
    def searchAction(self):
        message = self.studentNoEntry.validate(mode = "Search")
        valid = message[0]
        errorMessage = message[1]
        if valid:
            self.setScreenEntity(self.model.getStudent(self.getScreenEntity()))
            messagebox.showinfo("Success", "Student Found")
        else:
            messagebox.showerror("Failed",errorMessage)
        
    
    def newAction(self):
        result = messagebox.askquestion("New", "Are You Sure?", icon='warning')
        if result == "yes":
            self.clearFields()
    
    
    def saveAction(self):
        messages = []
        messages.append(self.studentNoEntry.validate(mode = "Save"))
        messages.append(self.lastNameEntry.validate(mode = "Save"))
        messages.append(self.firstNameEntry.validate(mode = "Save"))
        messages.append(self.selectedGender.validate(mode = "Save"))
        messages.append(self.programListbox.validate(mode = "Save"))
        
        valid = True
        errorMessages = []
        for status, message in messages:
            if not status:
                valid = False
                errorMessages.append(message)
        
        errorMessage = "Please check the following fields:\n" + ("\n".join(errorMessages))
        
        if valid:
            self.model.saveStudent(self.getScreenEntity())
            messagebox.showinfo("Success", "Student Has Been Saved")
        else:
            messagebox.showerror("Failed Saving Student",errorMessage)
    
    
    def deleteAction(self):
        message = self.studentNoEntry.validate(mode = "Delete")
        
        if message[0]:
            result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
            if result == "yes":
                self.model.deleteStudent(self.getScreenEntity())
                self.clearFields()
                messagebox.showinfo(title = "Success", message = "Student information successfully deleted")
        else:
            messagebox.showerror(title = "Not Found", message = "Student was not found")
            
                
            
    ## VALIDATION
    
    def validateStudentNumber(self, value, mode):
        value = str(value)
        isValid = True
        message = ""
        # Check if all characters are digits
        allDigits = True
        for char in value:
            if not isNumber(char):
                allDigits = False
                break
        if not allDigits:
            # Student number must be all digits
            isValid = False
            message = "Student Number may contain digits only"
        elif len(value) != 10:
            #Student number must be 10 digits
            isValid = False
            message = "Student Number must be 10 digits"
            
        if mode == "Save":
            pass
        elif mode == "Delete":
            if not self.model.studentNumberExists(value):
                # Student number must be existing
                isValid = False
                message = "Student Number must be of an existing student"
        elif mode == "Search":
            if not self.model.studentNumberExists(value):
                # Student number must be existing
                isValid = False
                message = "Student Number must be of an existing student"
        
        return (isValid, message)
    
    
    def validateLastName(self, value, mode):
        value = str(value)
        isValid = True
        message = ""
        if mode == "Save":
            if len(value.strip()) == 0: 
                isValid = False
                message = "Last Name"
        
        return (isValid, message)
    
    
    def validateFirstName(self, value, mode):
        value = str(value)
        isValid = True
        message = ""
        if mode == "Save":
            if len(value.strip()) == 0: 
                isValid = False
                message = "First Name"
        
        return (isValid, message)
    
    
    def validateGender(self, value, mode):
        isValid = True
        message = ""
        if mode == "Save":
            if value == "None" or value == None:
                isValid = False
                message = "Gender"

        
        return (isValid, message)
    
    
    def validateProgram(self, value, mode):
        isValid = True
        message = ""
        if mode == "Save":
            if value == None or value == "":
                isValid = False
                message = "Program"
        return (isValid, message)
        
    
    ## HELPER
    def clearFields(self):
        self.setScreenEntity(self.model.getBlankEntity())
    
    def getScreenEntity(self):
        interests = {
                "Sports"        : self.sportsCheckValue.get(),
                "Music"         : self.musicCheckValue.get(),
                "Arts"          : self.artsCheckValue.get(),
                "Science"       : self.scienceCheckValue.get(),
                "Technology"    : self.technologyCheckValue.get(),
                "Nature"        : self.natureCheckValue.get()
        }
        programSelection = self.programListbox.curselection()
        
        if not programSelection:
            program = None
        else:
            program = self.programListbox.get(programSelection)
            
        screenEntity = self.model.buildEntity(
                studentNo   = str(self.studentNoEntry.get()),
                lastName    = str(self.lastNameEntry.get()),
                firstName   = str(self.firstNameEntry.get()),
                gender      = str(self.selectedGender.get()),
                description = str(self.descriptionText.get("1.0",END)),
                program     = str(program),
                interests = interests
        )
        return screenEntity
    
    
    def setScreenEntity(self, entity):
        self._reassignEntryValue(self.studentNoEntry, entity.studentNo)
        self._reassignEntryValue(self.lastNameEntry, entity.lastName)
        self._reassignEntryValue(self.firstNameEntry, entity.firstName)
        self.selectedGender.set(entity.gender)
        self.descriptionText.delete(1.0, END)
        self.descriptionText.insert(END, entity.description)
        programIndex = self.model.getProgramIndex(entity.program)
        if programIndex == None:
            self.programListbox.selection_clear(0, END)
        else:
            self.programListbox.select_set(programIndex)
        
        self.sportsCheckValue.set(entity.interests["Sports"])
        self.musicCheckValue.set(entity.interests["Music"])
        self.artsCheckValue.set(entity.interests["Arts"])
        self.scienceCheckValue.set(entity.interests["Science"])
        self.technologyCheckValue.set(entity.interests["Technology"])
        self.natureCheckValue.set(entity.interests["Nature"])
    
    def _reassignEntryValue(self, entry, value):
        entry.delete(0, END) 
        entry.insert(0, value) 
    
        