from tkinter import *
class View(Frame):
    def __init__(self, master=None, model = None):
        super().__init__(master=master)
        
        self.model = model
        
        self.initializeWidgets()
        self.pack()
    
    def initializeWidgets(self):
        titleLabel = Label(self, text = "Student Information")
        titleLabel.grid(row = 0, column = 0)
        
        self.initializeInfoGroup1()
        self.initalizeInfoGroup2()
        self.initializeButtonGroup()
        
        
    def initializeInfoGroup1(self):
        # INFO GROUP 1: Student No, Last Name, First Name, Gender
        infoGroup1 = Frame(self, pady = 10)
        infoGroup1.grid(row = 1, column = 0)
        
        
        # Row 0
        studentNoLabel = Label(infoGroup1, text = "Student No.")
        self.studentNoEntry = Entry(infoGroup1)
        self.searchBtn = Button(infoGroup1, text = "Search")

        studentNoLabel.grid(row = 0, column = 0)
        self.studentNoEntry.grid(row = 0, column = 1)
        self.searchBtn.grid(row = 0, column = 2)
        
        # Row 1
        lastNameLabel = Label(infoGroup1, text = "Last Name")
        self.lastNameEntry = Entry(infoGroup1)
        lastNameLabel.grid(row = 1, column = 0)
        self.lastNameEntry.grid(row = 1, column = 1)
        
        firstNameLabel = Label(infoGroup1, text = "First Name")
        firstNameLabel.grid(row = 1, column = 3)
        self.firstNameEntry = Entry(infoGroup1)
        self.firstNameEntry.grid(row = 1, column = 4)
        
        # Row 2
        genderLabel = Label(infoGroup1, text = "Gender")
        self.maleRadio = Radiobutton(infoGroup1, text = "Male")
        self.femaleRadio = Radiobutton(infoGroup1, text = "Female")
        
        genderLabel.grid(row = 2, column = 0)
        self.maleRadio.grid(row = 2, column = 1)
        self.femaleRadio.grid(row = 2, column = 2)
        
        
    def initalizeInfoGroup2(self):
        infoGroup2 = Frame(self)
        infoGroup2.grid(row = 2, column = 0)
        
        # Column 1
        # Row 0
        column1 = Frame(infoGroup2, padx = 10, pady = 5)
        descriptionLabel = Label(column1, text = "Description")
        self.descriptionText = Text(column1, height = 10, width = 30)
        
        column1.grid(row = 0, column = 0, sticky = "N")
        descriptionLabel.grid(row = 0, column = 0, sticky = "W")
        self.descriptionText.grid(row = 1, column = 0)
        
        # Column 2
        column2 = Frame(infoGroup2, padx = 10, pady = 5)
        interestLabel = Label(column2, text = "Choose Interest")
        
        column2.grid(row = 0, column = 1, sticky = "N")
        interestLabel.grid(row = 0, column = 0)
        
        sportsCheck = Checkbutton(column2, text = "Sports")
        musicCheck = Checkbutton(column2, text = "Music")
        artsCheck = Checkbutton(column2, text = "Arts")
        scienceCheck = Checkbutton(column2, text = "Science")
        technologyCheck = Checkbutton(column2, text = "Technology")
        natureCheck = Checkbutton(column2, text = "Nature")
        
        sportsCheck.grid(row = 1, column = 0, sticky = "W")
        musicCheck.grid(row = 2, column = 0, sticky = "W")
        artsCheck.grid(row = 3, column = 0, sticky = "W")
        scienceCheck.grid(row = 4, column = 0, sticky = "W")
        technologyCheck.grid(row = 5, column = 0, sticky = "W")
        natureCheck.grid(row = 6, column = 0, sticky = "W")
        
        
        # Column 3
        column3 = Frame(infoGroup2, padx = 10, pady = 5)
        column3.grid(row = 0, column = 2, sticky = "N")
        
        programItems = ["BSIT", "BSCS", "BSIS", "BSBA", "BSCPE", "BSBN","BSECE"]
        programLabel = Label(column3, text = "Select Program")
        self.programListbox = Listbox(column3)
        for item in programItems: self.programListbox.insert(END, item)
        
        programLabel.grid(row = 0, column = 0)
        self.programListbox.grid(row = 1, column = 0)
        
        
    def initializeButtonGroup(self):
        actionGroup = Frame(self, pady = 10, padx = 40)
        actionGroup.grid(row = 3, column = 0, sticky = "E")
        
        self.deleteButton = Button(actionGroup, text = "Delete")
        self.newButton = Button(actionGroup, text = "New")
        self.saveButton = Button(actionGroup, text = "Save")
        
        self.deleteButton.pack(side = LEFT)
        self.newButton.pack(side = LEFT)
        self.saveButton.pack(side = LEFT)
    
    
    def initalizeActions(self):
        pass
    
        
        
    
root= Tk()
main = View(root)
root.mainloop()
