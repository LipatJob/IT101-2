from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    
    # Creation of init_windows
    def init_window(self):
        # Changing the title of the master widget
        self.master.title("GUI")
        
        # Creating label and entry
        lblFirstnum = Label(self, text = "First Number: ")
        lblSecondnum = Label(self, text = "Second Number: ")
        self.lblResult = Label(self, relief = RIDGE, width = 30)
        self.txtFirst = Entry(self, width = 20)
        self.txtSec = Entry(self, width = 20)
        
        # Creating a button instance
        btnAdd = Button(self, text = "Add", width = 7, command = self.getSum)
        btnQuit = Button(self, text = "Quit", width = 7, command = self.client_exit)
        
        # Organize widget and place them on the window
        lblFirstnum.grid(row = 0, column = 0, pady = 3)
        self.txtFirst.grid(row = 0, column = 1, columnspan = 2)
        lblSecondnum.grid(row = 1, column = 0, pady = 3)
        self.txtSec.grid(row = 1, column = 1, columnspan = 2)
        btnAdd.grid(row = 2, column = 1, pady = 3)
        btnQuit.grid(row = 2, column = 2)
        self.lblResult.grid(row = 3, column = 0, columnspan = 3)
        
        # Place the widget on the root window
        self.pack()
    
    def client_exit(self):
        exit()
    
    def getSum(self):
        firstNum = self.txtFirst.get()
        secNum = self.txtSec.get()
        a = int(firstNum) + int(secNum)
        self.lblResult.config(text = f"The anwer is {a}")
        
root = Tk()
# Resize the window
root.geometry("300x120")
app = Window(root)
root.mainloop()