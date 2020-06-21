from tkinter import *
from tkinter.font import Font
from Constants import *
import winsound

class GameCompleteView(Frame):
    def __init__(self, master=None, model = None, controller = None, **kw):
        super().__init__(master = master, **kw, bg = BG_COLOR)
        self.model = model
        self.controller = controller
        self.initComponents()
    
    """ INITIALIZATION """
    def initComponents(self):
        titleFont = Font(size = 40, family = "helvetica", weight = "bold")
        messageFont = Font(size = 20, family = "helvetica" )
        self.titleLabel = Label(self, text = "Congratulations", bg = BG_COLOR, font = titleFont, fg = "white")
        self.messageLabel = Label(self, text = "You have finished all levels!", bg = BG_COLOR, font = messageFont, fg = 'white')
        self.restartButton = EndButton(self, text = "Restart Game", command = self.__restartGame)
        self.mainMenu = EndButton(self, text = "Main Menu", command = self.__mainmenu)
        
        self.titleLabel.pack(side = TOP)
        self.messageLabel.pack(side = TOP, pady = 20)
        self.restartButton.pack(side = TOP, pady = 5)
        self.mainMenu.pack(side = TOP, pady = 5)
        
        self.pack(expand = True, pady = (0, 100))
        
    """ ACTIONS """
    def __restartGame(self):
        winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
        self.controller.restartGame()
        
    def __mainmenu(self):
        winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
        self.controller.titleView()



""" STYLED COMPONENTS """
class EndButton(Button):
    def __init__(self, master = None, origParent = None, **kw):
        self.origParent = origParent
        
        self.endPic = PhotoImage(file = END_BUTTON_PICTURE)
        font = Font(size = 18, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.endPic, 
                         height = 62, width = 236, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR, fg = "white", activeforeground = "white",
                         font = font, compound="c")

   