""" 
Please open README.md using a markdown editor to see the functionalities of the modules 

Recommended Checking Order:
__main__.py
/src/Controller.py
/src/LevelModel.py

# UI
/src/views/LevelView.py
/src/views/GameCompleteView.py
/src/views/TitleScreenView.py

# file handling
/src/entities/GameState.py
/src/entities/Levels.py
/lib/FileBound # Allows classes to specify how to be serialized
/lib/FileDataHandler # Encapsulation of a file

# files
/data/gamestate.json # Where the currentlevel data and coins are stored
/data/levels.json # Where the level data is stored
/assets/pics/* # pictures used
/assets/sound/* # audio used
/assets/* # Picture of styled components

"""
from tkinter import messagebox
from src.Controller import Controller
def main():
    try:
        controller = Controller()
        controller.mainView()
    except:
        messagebox.showerror(title = "Error", message = "The program has unexpectedly crashed. Please contact the developers")

if __name__ == "__main__":
    main()
    
    
    


