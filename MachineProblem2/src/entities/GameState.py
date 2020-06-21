from lib.FileBound import FileBound
from lib.filestrategy.JsonStrategy import JsonDecoder, JsonEncoder
from lib.FileDataHandler import FileDataHandler
import os

class GameState:
    def __init__(self, level = 0, coins = 100, deletedLetters = [], revealedLetters = []):
        self.level = level
        self.coins = coins
        self.deletedLetters = deletedLetters
        self.revealedLetters = revealedLetters
        
    def restart(self):
        self.level = 1
        self.coins = 100
        self.deletedLetters = []
        self.revealedLetters = []
        
        
class FileBoundGameStateFactory:
    def create(self):
        encoder = JsonEncoder()
        decoder = JsonDecoder()
        cwd = os.getcwd()
        fileHandler = FileDataHandler(cwd + "\\data\\gamestate.json")
        return FileBoundGameState(fileHandler, decoder, encoder)

class FileBoundGameState(GameState, FileBound):
    def __init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy):
        GameState.__init__(self)
        FileBound.__init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy)
    
    def toSerializable(self):
        return {
            "Level" : self.level,
            "Coins" : self.coins,
            "DeletedLetters" : self.deletedLetters,
            "RevealedLetters" : self.revealedLetters
        }
    
    def setData(self, data):
        if data == []:
            self.level = 1
            self.coins = 100
            self.deletedLetters = []
            self.revealedLetters = []
        else:
            self.level = data["Level"]
            self.coins = data["Coins"]
            self.deletedLetters = data["DeletedLetters"]
            self.revealedLetters = data["RevealedLetters"]
            
    