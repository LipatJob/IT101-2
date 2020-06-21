from tkinter import *
import os

class Window(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.continents = {"Asia":["Philippines","Malaysia","Taiwan","Singapore","Thailand","India"],
                            "Africa":["Algeria","Angola","Egypt","Cape Verde","Liberia","Kenya","Morocco","Nigeria"],
                            "America":["Venezuela","Peru","Jamaica","United States","Cuba","Chile","Argentina"],
                             "Europe":["Russia","Germany","United Kingdom","Italy", "Ukraine","France","Belgium"]}
        self.initComponents()
        
        
    def initComponents(self):
        # Setup Radio Buttons. Frame One
        radioFrame = Frame(self, padx = 10, pady = 5)
        self.radioValue = StringVar(radioFrame)
        
        #Dynamically Add Radio Buttons
        for continent in self.continents.keys():
            radio = Radiobutton(radioFrame, text = continent, value = continent, 
                                variable = self.radioValue, command = self.radioButtonSelect,
                                font = "Times 10 bold", fg= "blue", bg = "white",
                                padx = 20, relief = RIDGE)
            radio.pack(side = LEFT)
        radioFrame.pack(side = TOP)
            
        # Setup Scrollbar and Listbox. Frame Two
        scrollFrame = Frame(self, padx = 10)
        scroll = Scrollbar(scrollFrame, orient = VERTICAL)
        self.countryList = Listbox(scrollFrame, yscrollcommand = scroll.set, font = "Times 20", width = 10)
        scrollFrame.pack(side = LEFT)
        scroll.pack(side = RIGHT, fill = Y)
        self.countryList.pack()
        self.countryList.bind('<<ListboxSelect>>', self.listBoxSelect)
        
        # Setup Image Frame. Frame Three
        imageFrame = Frame(self, pady = 5, padx = 5)
        self.image = Label(imageFrame, relief = RIDGE)
        imageFrame.pack(side = LEFT)
        self.image.pack()
        
        # Set initial Values
        self.radioValue.set(list(self.continents.keys())[0])
        self.countryList.selection_set(0)
        self.radioButtonSelect()
        self.listBoxSelect()
    
    
    def radioButtonSelect(self):
        self.loadCountries(str(self.radioValue.get()))
        self.countryList.selection_set(0)
        self.listBoxSelect()
    
    
    def listBoxSelect(self, *args):
        country = self.countryList.get(self.countryList.curselection()[0])
        self.loadImage(country)
        
        
    def loadCountries(self, continent):
        self.countryList.delete(0, END)
        for country in self.continents[continent]:
            self.countryList.insert(END, country)
    
        
    def loadImage(self, country):
        image = PhotoImage(file = country + ".png")
        self.image.configure(image = image)
        self.image.image = image


root = Tk()
root.geometry("500x200")
root.title("LT_LipatJob")
mainWindow = Window(root)
mainWindow.pack()
root.mainloop()
        
