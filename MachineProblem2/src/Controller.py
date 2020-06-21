from src.LevelModel import LevelModelFactory
from src.views.LevelView import LevelView
from src.views.GameCompleteView import GameCompleteView
from src.views.TitleScreenView import TitleScreenView
from tkinter import Tk, Frame, PhotoImage
from Constants import *

class Controller:
    """ 
    The Controller is the director of the program. Other modules of the programs ask the controller where to go next.
    For example, after completing a level, the level view informs the controller that the level is done. The controller
    then directs the frame to the next level
    """
    def __init__(self):
        self.root = Tk()
        # Configure Window
        self.favico = PhotoImage(file = FAVICO)
        self.root.tk.call('wm', 'iconphoto', self.root._w, self.favico)
        self.root.title(WINDOW_TITLE)
        self.root.geometry(SCREEN_SIZE)
        self.root.configure(bg = BG_COLOR)
        self.root.resizable(False, False)
        self.mainFrame = Frame(self.root)
    
    
    def mainView(self):
        self.mainFrame.destroy()
        self.model = LevelModelFactory().create()
        self.titleView()
        self.root.mainloop()
        
        
    def titleView(self):
        self.mainFrame.destroy()
        self.mainFrame = TitleScreenView(self.root, model = self.model, controller = self)
    
    
    def startGame(self):
        self.mainFrame.destroy()
        if self.model.getLevel() > LAST_LEVEL:
            self.mainFrame = GameCompleteView(self.root, model = self.model, controller = self)
        else:
            self.mainFrame = LevelView(self.root, self.model, controller = self)
        self.mainFrame.pack()
    
    
    def nextLevel(self):
        self.mainFrame.destroy()
        self.model.nextLevel()
        self.startGame()
    
    
    def restartGame(self):
        self.model.restart()
        self.titleView()
    
    
    
        
    
        
          
        