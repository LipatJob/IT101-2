from tkinter import * 
from tkinter.font import Font
from Constants import *
from tkinter import messagebox
import winsound
import random
import time

class LevelView(Frame):
    """ The view is the UI of the application. it is recommened to use a text editor that folds code in this section"""
    def __init__(self, master=None, model = None, controller = None, **kw):
        super().__init__(master = master, **kw, bg = BG_COLOR)
        self.model = model
        self.controller = controller
        self.pics = []
        
        self.initComponents()
        self.pack(expand = True, fill = BOTH)
    
    """ INITIALIZATIONS """
    def initComponents(self):
        self.initHeader()
        self.initPicture()
        letterFrame = LettersFrame(self, self.model, onwin = self.onwin)
        letterFrame.pack()
    
    
    def initHeader(self):
        # Initialize Header
        headerFont = Font(size = "12", weight = "bold", family = "Helvetica")
        headerFrame = Frame(self, bg = HDR_COLOR)
        headerFrame.pack(fill = X, side = TOP, anchor = "n", ipady = 0, pady = (0, 25))

        # Main Menu
        innerPad = 20
        def mainMenu():
            winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
            self.controller.titleView()
        
        self.MainMenuButton = MainMenuButton(headerFrame, command = mainMenu)
        self.MainMenuButton.pack(side = LEFT, anchor = "w", padx = (innerPad, 0))
        
        # Level
        self.levelFrame = LevelFrame(headerFrame, str(self.model.getLevel()))
        self.levelFrame.pack(side = LEFT, expand = True, anchor = "center")
        
        # Coins
        coinFrame = Frame(headerFrame, bg = HDR_COLOR, width = 100)
        coinFrame.pack(side = LEFT, anchor = "e", padx = (0, innerPad))
        
        self.coinsLabel = Label(coinFrame, text = str(self.model.getCoins()), bg = HDR_COLOR, fg = "white", font = headerFont)
        self.coinsLabel.pack(side = LEFT)
        self.coinPicture = PhotoImage(file = COIN_PICTURE)
        pictureLabel = Label(coinFrame, image = self.coinPicture,  bg = HDR_COLOR)
        pictureLabel.pack(side = LEFT)
    
        
    def initPicture(self):
         # Initialize Picture
        self.picture = PhotoImage(file = self.model.getPicture())
        pictureLabel = Label(self, image = self.picture, borderwidth = 0, relief='flat', bg = BG_COLOR)
        pictureLabel.pack(pady = (0, 20))
    
    
    """ ACTIONS """
    def onwin(self, skipped = False):
        if not skipped:
            self.model.increaseCoins(10)
        self.controller.nextLevel()
    
    
    def updateCoins(self):
        self.coinsLabel['text'] = str(self.model.getCoins())
    

    
    
class LettersFrame(Frame):
    def __init__(self, master = None, model = None, onwin = None, **kw):
        super().__init__(master = master, **kw, bg = BG_COLOR)
        self.model = model
        self.onwin = onwin
        
        self.selectionFrame = Frame(self, bg = BG_COLOR)
        self.guessFrame = Frame(self, bg = BG_COLOR)
        
        self.initSelectionFrame()
        self.initGuessFrame()
        self.initGameState()
        
        self.guessFrame.pack(pady = (10, 20))
        self.selectionFrame.pack(pady = (0,0))
            
    """ INITIALIZATIONS """
    def initSelectionFrame(self):
        self.buttonFrames = []
        
        # Get word and get randomized selection of letters
        word = self.model.getWord()
        letters = self.model.createRandomSelection(word, self.model.getLevel())
        
        # Create 6x2 selection
        for index, letter in enumerate(letters):
            # Create Button Frame
            tempFrame = BlankButtonFrame(self.selectionFrame)
            tempFrame.grid(row = index // 6, column = index % 6, padx = 3, pady = 3)
            self.buttonFrames.append(tempFrame)
            
            # Check if letter is deleted
            if self.model.isDeleted(index):
                # Dont create button if letter is deleted
                continue
            
            #Create button
            button = SelectionButton(tempFrame, text = letter.upper(), origParent = tempFrame)
            def buttonCommand(button):
                def move():
                    self.moveToGuess(button)
                return move
            button.configure(command = buttonCommand(button))
            tempFrame.origButton = button
            button.pack()
        
        # Create Lifeline buttons
        revealFrame = Frame(self.selectionFrame, height = BTN_SIZE, width = BTN_SIZE)
        self.revealLetterButton = RevealLetterButton(revealFrame)
        self.revealLetterButton.configure(command = self.revealSingleLetter)
        self.revealLetterButton.pack()
        revealFrame.grid(row = 0, column = 6, padx = 3, pady = 3)
        
        skipFrame = Frame(self.selectionFrame, height = BTN_SIZE, width = BTN_SIZE)
        self.skipLevelButton = SkipLevelButton(skipFrame)
        self.skipLevelButton.configure(command = self.skipLevel)
        self.skipLevelButton.pack()
        skipFrame.grid(row = 1, column = 6, padx = 3, pady = 3)
        
        
    def initGuessFrame(self):
        self.guesses = []
        word = self.model.getWord()
        
        # Create frames from letters of the word
        for letter in word:
            tempFrame = BlankGuessFrame(self.guessFrame)
            tempFrame.pack(side = LEFT, padx = 3, pady = 3)
            # 0 -> frame itself
            # 1 -> child frame
            # 2 -> revealed or not
            self.guesses.append([tempFrame, None, False])
    
    
    def initGameState(self):
        # Move buttons that are revealed to Guess
        for indices in self.model.getRevealed():
            # 0 -> selection 
            # 1 -> guess
            self.moveToGuessIndex(self.buttonFrames[indices[0]].origButton, indices[1])
            self.guesses[indices[1]][2] = True
            self.buttonFrames[indices[0]].origButton.config(fg = "#82d300", activeforeground = "#82d300", command = lambda : True)
    
    """ ACTIONS """
    def moveToGuess(self, button):
        # Select Spot for New Button
        for index, guess in enumerate(self.guesses):
            if guess[1] == None:
                self.moveToGuessIndex(button, index)
                winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
                break
            
        #2ms to allow click sound to play
        self.after(2, self.checkGameState)
    
    
    def moveToGuessIndex(self, button, index):
        #Create new button
        guess = self.guesses[index]
        newButton = self.__toGuessButton(button, guess[0])
        newButton.pack()
        guess[1] = newButton
        
        #Dispose Old Button
        self.update()
    
    
    def moveToSelection(self, button):
        # Create New Button
        newButton = self.__toSelectionButton(button)
        newButton.pack()
        winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
    
    
    def checkGameState(self):
        # Checks if theuser has won
        word = self.model.getWord()
        guesses = []
        
        # Build guess
        for place in self.guesses:
            if place[1] == None:
                return False
            guesses.append(place[1]['text'])
        
        correctGuess = True
        # Check guess
        for guess, letter in zip(word, guesses):
            if guess.lower() != letter.lower():
                correctGuess = False
                break
        
        # Styles when correct or wrong
        def turnTextRed():
            for place in self.guesses:
                if place[2]:
                    continue
                place[1].configure(fg = "red")
                    
        def turnTextWhite():
            for place in self.guesses:
                if place[2]:
                    continue
                if place[1] != None:
                    place[1].configure(fg = "white")
                
        def turnTextGreen():
            for place in self.guesses:
                if place[1] != None:
                    place[1].configure(fg = "#82d300")
                
        if not correctGuess:
            # Play Sound
            winsound.PlaySound(INCORRECT_SOUND_FILE, winsound.SND_ASYNC)
            turnTextRed()     
            self.after(400, turnTextWhite)
        else:
            # Play Sound
            winsound.PlaySound(CORRECT_SOUND_FILE, winsound.SND_ASYNC)
            turnTextGreen()
            self.after(700, lambda : self.onwin())
            
            
        return correctGuess


    """ HINTS """
    def revealSingleLetter(self):
        # Find all available indices in Guess Index
        tempGuesses = self.guesses
        availableIndices = []
        for index, frame in enumerate(tempGuesses):
            if frame[2] == False:
                availableIndices.append(index)
        
        # Cannot reveal letter when there are no available indices
        if len(availableIndices) < 1:
            return False
        
        # Shuffle available indices and get the first index as target frame and letter
        random.shuffle(availableIndices)
        index = availableIndices[0]
        targetFrame = self.guesses[index]
        targetLetter = self.model.getWord()[index].lower()
        
        # Messages
        if self.model.getCoins() - REVEAL_LETTER_COST < 0:
            # If insufficient coins
            messagebox.showwarning(title = "Cannot Reveal Letter", message = f"Not Enough Coins!\nRevealing a letter costs {REMOVE_LETTER_COST} coins")
            return False
        
        selection = messagebox.askquestion ('Reveal Letter',f'Do you want to spend {REMOVE_LETTER_COST} coins to reveal a letter?',icon = 'info')
        if selection == "no":
            # Confirm
            return False
        
        # Remove letter from guess frame if exists
        if targetFrame[1] != None:
            self.moveToSelection(targetFrame[1])
        
        # Find first letter that in the selection box that is equal to the target letter
        for selectionIndex, frame in enumerate(self.buttonFrames):
            if frame.origButton != None and frame.origButton['text'].lower() == targetLetter:
                # If found move to guess and remove command
                self.moveToSelection(frame.origButton)
                self.moveToGuessIndex(frame.origButton, index)
                winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
                
                self.after(2, lambda : True)
                frame.origButton.config(fg = "#82d300", activeforeground = "#82d300", command = lambda : True)
                self.guesses[index][2] = True
                self.model.addRevealed([selectionIndex, index])
                self.checkGameState()
                frame.origButton = None
                break
        
        # Update other components
        self.model.decreaseCoins(REMOVE_LETTER_COST)
        self.master.updateCoins()
        return True
        
    
    def skipLevel(self):
        # Messages
        if self.model.getCoins() - SKIP_COST < 0:
            # If insufficient coins
            messagebox.showwarning(title = "Cannot Skip Level", message = f"Not Enough Coins!\nSkipping Level Costs {SKIP_COST} coins")
            return
        
        selection = messagebox.askquestion ('Skip Level',f'Do you want to spend {SKIP_COST} coins to skip the level?',icon = 'info')
        if selection == "no":
            # Confirm action
            return
        
        self.revealLetters()
        self.model.decreaseCoins(SKIP_COST + LEVEL_REWARD)

 
    def revealLetters(self):
        # Disable all buttons
        self.revealLetterButton["state"] = "disabled"
        self.skipLevelButton["state"] = "disabled"
        for frame in self.buttonFrames:
            if frame.origButton != None:
                frame.origButton["state"] = "disabled"
        
        revealed = set()
        # Clear Guesses and get Letters that have been revealed
        for index, letter in enumerate(self.guesses):
            if(letter[2]):
                # check if letter is revealed
                revealed.add(index)
            if letter[1] != None and letter[2] == False:
                def move():
                    origParent = letter[1].origParent
                    self.moveToSelection(letter[1])
                    origParent.origButton["state"] = "disabled"
                self.after(170,move())
        
        # Loop through letters of the word
        word = self.model.getWord()
        for index, letter in enumerate(word):
            if index in revealed:
                continue
            # Search the Button Frames with the same letter
            for frame in self.buttonFrames:
                # If found, move letter to guess
                if len(frame.winfo_children()) > 0 and frame.origButton['text'].lower() == letter:
                    self.after(170,self.moveToGuess(frame.origButton))
                    break
    
    
    def deleteLetter(self):
        """ 
        Author's Notes: Unfortunately, I thought that one of the lifelines was Delete Letter.
        It turned out it was supposed to be reveal letter 
        """
        word = self.model.getWord()
        
        # List Down All Button Frames
        frames = []
        for index, buttonFrame in enumerate(self.buttonFrames):
            if buttonFrame.origButton != None:
                frames.append((index, buttonFrame))
        random.shuffle(frames)
        
        
        # eg.  Word: PYTHON -> {P: 0, Y:0, T: 0, H: 0, O:0, N:0}
        # Create Dictionary of Letters of Words
        wordLetters = {}
        for letter in word:
            if letter.lower() not in wordLetters:
                wordLetters[letter.lower()] = 0
        
        # eg.  Selection: PPYYTHON -> {P: 2, Y:2, T: 1, H: 1, O:1, N:1}
        # List down Frequency of Letters of Words in Selection
        for frame in frames:
            letter = frame[1].origButton['text'].lower()
            if letter in wordLetters:
                wordLetters[letter] += 1
                
        # eg.  {P: 2, Y:2, T: 1, H: 1, O:1, N:1} - {P: 1, Y:1, T: 1, H: 1, O:1, N:1}  = {P:1, Y:1, T: 0, H: 0, O:0, N:0}
        # This means that 1 "P" and 1 "Y" tile can be deleted
        # Subtract Frequency of Letters in Words 
        for letter in word:
            if letter.lower() not in wordLetters:
                wordLetters[letter.lower()] = 0
            wordLetters[letter.lower()] -= 1
        
        # Get All Frames that can be Deleted
        availableLetters = []
        for frame in frames:
            letter = frame[1].origButton['text'].lower()
            if letter not in wordLetters:
                availableLetters.append(frame)
            else:
                if wordLetters[letter] > 0:
                    availableLetters.append(frame)
                    wordLetters[letter] -= 1

        # Messages
        if len(availableLetters) == 0:
            # Return False If Cannot Delete
            messagebox.showwarning(title = "Cannot Delete", message = "Maximum words deleted reached")
            return False
        
        if self.model.getCoins() - REMOVE_LETTER_COST < 0:
            messagebox.showwarning(title = "Cannot Delete", message = f"Not Enough Coins!\nDeleting a letter costs {REMOVE_LETTER_COST} coins")
            return False
        
        selection = messagebox.askquestion ('Delete Letter',f'Do you want to spend {REMOVE_LETTER_COST} coins to delete a letter?',icon = 'info')
        if selection == "no":
            return False
        
        toDelete = availableLetters[0]
        
        # Dispose From Guesses
        for guess in self.guesses:
            if guess[1] == toDelete[1].origButton:
                guess[1] = None
        # Dispose Letter
        toDelete[1].origButton.destroy()
        # Dispose From Frame
        self.buttonFrames[toDelete[0]]
        self.buttonFrames[toDelete[0]].origButton = None
        
        # Update model and view
        self.model.deleteLetter(toDelete[0])
        self.model.decreaseCoins(REMOVE_LETTER_COST)
        self.master.updateCoins()
        
        winsound.PlaySound(CLICK_SOUND_FILE, winsound.SND_ASYNC)
        
        # Return True When Deleted Successfuly
        return True
    
    
    """ Helper """
    def __toSelectionButton(self, button):
        # Copy paste data into new button
        origParent = button.origParent
        newButton = SelectionButton(origParent, text = button['text'].upper(), origParent = origParent)
        newButton.configure(command = lambda : self.moveToGuess(newButton))
        origParent.origButton = newButton
        
        # Destory Old Button
        for index, place in enumerate(self.guesses):
            if place[1] == button:
                self.guesses[index][1] = None
                break
        button.destroy()
        
        self.update()
        return newButton
    
    
    def __toGuessButton(self, button, target):
        # Copy paste data into new button
        origParent = button.origParent
        newParent = target
        newButton = GuessButton(newParent, origParent = origParent, text = button['text'])
        newButton.config(command = lambda : self.moveToSelection(newButton))
        origParent.origButton = newButton
        
        # Destory Button        
        button.destroy()
        return newButton
        
        
    

""" STYLED COMPONENTS """

class SelectionButton(Button):
    def __init__(self, master = None, origParent = None, **kw):
        self.origParent = origParent
        
        self.buttonPic = PhotoImage(file = "./assets/button.png")
        font = Font(size = 26, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.buttonPic, 
                         height = 60, width = 60, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR, activeforeground = "black" , 
                         font = font, compound="c")
        
class GuessButton(Button):
    def __init__(self, master = None, origParent = None, **kw):
        self.origParent = origParent
        
        self.guessPic = PhotoImage(file = "./assets/guess.png")
        font = Font(size = 26, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.guessPic, 
                         height = 50, width = 50, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR, fg = "white", activeforeground = "white",
                         font = font, compound="c")
        
class DeleteLetterButton(Button):
    def __init__(self, master = None, origParent = None, letter = "", **kw):
        self.origParent = origParent
        self.letter = letter
        
        self.guessPic = PhotoImage(file = "./assets/deleteLetter.png")
        font = Font(size = 26, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.guessPic, 
                         height = 60, width = 60, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR,
                         font = font, compound="c")
        
class SkipLevelButton(Button):
    def __init__(self, master = None, origParent = None, letter = "", **kw):
        self.origParent = origParent
        self.letter = letter
        
        self.guessPic = PhotoImage(file = "./assets/skip.png")
        font = Font(size = 26, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.guessPic, 
                         height = 60, width = 60, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR,
                         font = font, compound="c")
   
class BlankButtonFrame(Canvas):
    def __init__(self, master = None, origButton = None, **kw):
        super().__init__(master=master, **kw, width = 60, height = 60, 
                         borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR)
        self.origButton = origButton
        self.blankPic = PhotoImage(file = "./assets/blankbuttonframe.png")
        self.create_image(0,0, anchor = NW, image = self.blankPic)
        
class BlankGuessFrame(Canvas):
    def __init__(self, master = None, **kw):
        super().__init__(master=master, **kw, width = 50, height = 50, 
                         borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR)
        
        self.blankPic = PhotoImage(file = "./assets/guess.png")
        self.create_image(0,0, anchor = NW, image = self.blankPic)
    
class LevelFrame(Canvas):
    def __init__(self, master = None, text = "", **kw):
        super().__init__(master=master, **kw, width = 45, height = 45, 
                         borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = HDR_COLOR)
        
        self.levelPic = PhotoImage(file = "./assets/level.png")
        self.create_image(0,0, anchor = NW, image = self.levelPic)
        levelFont = Font(size = "14", weight = "bold", family = "Helvetica")
        self.create_text(45//2, 45//2 ,text = text, anchor = "center", fill = "white", font = levelFont)
        
class MainMenuButton(Button):
    def __init__(self, master = None, origParent = None, **kw):
        self.origParent = origParent
        
        self.guessPic = PhotoImage(file = "./assets/back.png")
        font = Font(size = 26, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.guessPic, 
                         height = 30, width = 30, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = HDR_COLOR, activebackground = HDR_COLOR, fg = "white",
                         font = font, compound="c")
        
class RevealLetterButton(Button):
    def __init__(self, master = None, origParent = None, letter = "", **kw):
        self.origParent = origParent
        self.letter = letter
        
        self.guessPic = PhotoImage(file = "./assets/revealletter.png")
        font = Font(size = 26, family = "Helvetica", weight = "bold")
        super().__init__(master=master, **kw, image = self.guessPic, 
                         height = 60, width = 60, borderwidth = 0, highlightthickness = 0, relief='flat', 
                         bg = BG_COLOR, activebackground = BG_COLOR,
                         font = font, compound="c")
        
        

