from tkinter import *
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window() # Contains the widgets
        
    def init_window(self):
        # Shared variable of the radio buttons
        self.v = StringVar()
        self.v.set("red") # Set default value
        
        # Create message widget
        self.msgResult = Message(self, text = "One Malayan, Proud Malayan", width = 250, font = "times 10")
        
        # Create Radio Buttons
        optRed = Radiobutton(self, text ="Red", variable = self.v, value = "red", command = self.changeColor)
        optYellow = Radiobutton(self, text ="Yellow", variable = self.v, value = "yellow", command = self.changeColor)
        optGreen = Radiobutton(self, text ="Green", variable = self.v, value = "green", command = self.changeColor)
        
        
        # Variables for CheckButtons
        self.b = StringVar()
        self.i = StringVar()
        self.l = StringVar()
        
        # Create Checkbuttons
        chckBold = Checkbutton(self, text = "BOLD", font = "times 12 bold", variable = self.b, onvalue = "bold", offvalue = "", command = self.changeStyle)
        chckItalic = Checkbutton(self, text = "ITALIC", font = "times 12 italic", variable = self.i, onvalue = "italic", offvalue = "", command = self.changeStyle)
        chckLine = Checkbutton(self, text = "UNDERLINE", font = "times 12 underline", variable = self.l, onvalue = "underline", offvalue = "", command = self.changeStyle)
        
        
        # Create Spinbox
        self.spnSize = Spinbox(self, from_ = 10, to = 20, width = 5, command = self.changeStyle)
        
        # Create Listbox with scrollbar in a frame
        frmlist = Frame(self)
        self.lstStyle = Listbox(frmlist, font = "Times 15", width = 10, height = 5)        
        self.lstStyle.pack(side = LEFT)
        scrollbar = Scrollbar(frmlist, orient = VERTICAL)
        scrollbar.pack(side= RIGHT, fill = Y)
        
        # Add items in the listbox using insert()
        style = ['Helvetica', 'Courier', "Times", "Verdana", "Symbol", "System"]
        i = 0
        for x in style:
            self.lstStyle.insert(i, x)
            i += 1
            
        self.lstStyle.selection_set(0) # Set first item in the list as default selected
        scrollbar.config(command = self.lstStyle.yview)
        self.lstStyle.bind('<<ListboxSelect>>', self.changeStyle)
        
        
        # Organize widgets
        optRed.grid(row = 0, column = 1)
        optYellow.grid(row = 0, column = 2)
        optGreen.grid(row = 0, column = 3)
        self.msgResult.grid(row = 2, column = 1, columnspan = 3)
        
        chckBold.grid(row = 1, column = 1)
        chckItalic.grid(row = 1, column = 2)
        chckLine.grid(row = 1, column = 3)
        
        # Create label and place on window
        Label(self, text = "Size").grid(row = 0, column = 4, sticky = "sw")
        self.spnSize.grid(row = 1, column = 4, sticky = "nw", pady = 5, padx = 5)
        
        frmlist.grid(row = 0, rowspan = 4, column = 0)
        
        
        # Place widgets on the window
        self.pack()
        
    def changeColor(self):
        self.msgResult.config(fg = str(self.v.get()))
        
    def changeStyle(self, *args):
        n = self.spnSize.get()
        stylo = self.lstStyle.get(self.lstStyle.curselection()[0])
        st = f"{str(stylo)} {str(n)} {str(self.b.get())} {str(self.i.get())} {str(self.l.get())}"
        self.msgResult.config(font = st)


root = Tk()
root.geometry("450x130")
app = Window(root)
root.title("PL9-2")
root.mainloop()