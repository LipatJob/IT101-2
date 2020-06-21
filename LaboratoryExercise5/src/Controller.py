from src.entities.Student import FileBoundStudentsFactory
from src.Model import Model
from src.views.MainView import MainView
from tkinter import Tk

class Controller:
    def __init__(self):
        self.root = Tk()
        self.root.title("LabExer #5")
        self.root.resizable(False, False)
        

    def mainView(self):
        students = FileBoundStudentsFactory().create()
        students.retrieveState()
        model = Model(students)
        mainView = MainView(self.root, model)
        mainView.pack()
        self.root.mainloop()
        
          
        