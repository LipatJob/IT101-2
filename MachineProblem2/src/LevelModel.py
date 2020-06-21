from src.entities.GameState import *
from src.entities.Levels import *
import os, random
        
class LevelModel:
    """
    The Model is the intermediate class between the view and the data. The view queries the model if
    it needs a certain data.
    """
    def __init__(self, gameStateEntity = None, levelsEntity = None):
        self.gameStateEntity = gameStateEntity
        self.levelsEntity = levelsEntity
        
    def createRandomSelection(self, word, seed):
        """ Creates a random selection of words using the level as the seed"""
        falseChoices = 12 - len(word)
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
                    "i", "j", "k", "l", "m", "n", "o", "p",
                    "q", "r", "s", "t", "u", "v", "w", "x",
                    "y", "z"]
        wordLetters = [char for char in word.lower()]
        random.seed(seed)
        falseLetters = random.choices(alphabet, k = falseChoices)
        letterSelection = falseLetters + wordLetters
        random.seed(seed)
        random.shuffle(letterSelection)
        return letterSelection
    
    def restart(self):
        self.gameStateEntity.restart()
        self.gameStateEntity.saveState()
    
    def getPicture(self):
        levelNumber = self.gameStateEntity.level
        file = self.levelsEntity.levelData[str(levelNumber)]["file"]
        return os.getcwd() + "\\assets\\pics\\resized\\" + file
    
    def getWord(self):
        levelNumber = self.gameStateEntity.level
        return self.levelsEntity.levelData[str(levelNumber)]["word"]
    
    def getLevel(self):
        return self.gameStateEntity.level
    
    def getCoins(self):
        return self.gameStateEntity.coins
    
    def getRevealed(self):
        return self.gameStateEntity.revealedLetters
    
    def addRevealed(self, index):
        self.gameStateEntity.revealedLetters.append(index)
        self.gameStateEntity.saveState()
    
    def deleteLetter(self, index):
        self.gameStateEntity.deletedLetters.append(index)
        self.gameStateEntity.saveState()
    
    def increaseCoins(self, coins):
        self.gameStateEntity.coins += coins
        self.gameStateEntity.saveState()
    
    def decreaseCoins(self, coins):
        self.gameStateEntity.coins -= coins
        self.gameStateEntity.saveState()
    
    def isDeleted(self, index):
        return index in self.gameStateEntity.deletedLetters
        
    def nextLevel(self):
        self.gameStateEntity.level += 1
        self.gameStateEntity.deletedLetters = []
        self.gameStateEntity.revealedLetters = []
        self.gameStateEntity.saveState()
    





class LevelModelFactory():
    def create(self):
        gameStateEntity = FileBoundGameStateFactory().create()
        levelsEntity = FileBoundLevelsFactory().create()
        gameStateEntity.retrieveState()
        levelsEntity.retrieveState()
        return LevelModel(gameStateEntity, levelsEntity)