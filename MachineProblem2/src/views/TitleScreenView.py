from tkinter import *
from tkinter.font import Font
from Constants import *
import winsound

class TitleScreenView(Frame):
    def __init__(self, master=None, model = None, controller = None, **kw):
        super().__init__(master = master, **kw, bg = BG_COLOR)
        self.model = model
        self.controller = controller
        self.initComponents()
    
    
    """ INITIALIZATIONS """
    def initComponents(self):
        self.logo = LogoFrame(self)
        self.level = LevelFrame(self, text = self.model.getLevel())
        self.playButton = PlayButton(self, text = "Play", command = self.__startGame )
        
        self.level.pack(side = TOP, pady = 20)
        self.logo.pack(side = TOP)
        self.playButton.pack(side = TOP, pady = 30)
        
        self.pack(expand = True, pady = (0, 100))
        
        
    """ ACTIONS """
    def __startGame(self):
        winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
        self.controller.startGame()


class PlayButton(Button):
    def __init__(self, master = None, origParent = None, **kw):
        self.origParent = origParent
        
        self.playPic = PhotoImage(file = PLAY_PICTURE)
        font = Font(size = 30, family = "Segoe UI", weight = "bold")
        super().__init__(master=master, **kw, image = self.playPic, 
                         height = 91, width = 266, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR, fg = "white", activeforeground = "white",
                         font = font, compound="c")


class LevelFrame(Canvas):
    def __init__(self, master = None, text = "", **kw):
        super().__init__(master=master, **kw, width = 70, height = 70, 
                         borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR)
        
        self.levelPic = PhotoImage(file = TITLE_LEVEL_PICTURE)
        self.create_image(0,0, anchor = NW, image = self.levelPic)
        levelFont = Font(size = "20", weight = "bold", family = "Helvetica")
        self.create_text(70//2, 70//2 ,text = text, anchor = "center", fill = "white", font = levelFont)


class LogoFrame(Canvas):
    def __init__(self, master = None, **kw):
        super().__init__(master=master, **kw, width = 300, height = 300, 
                         borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR)
        
        self.blankPic = PhotoImage(file = TITLE_PICTURE)
        self.create_image(0,0, anchor = NW, image = self.blankPic)
   