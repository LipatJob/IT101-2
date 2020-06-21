from lib.FileBound import FileBound
from lib.filestrategy.JsonStrategy import JsonDecoder, JsonEncoder
from lib.FileDataHandler import FileDataHandler
import os

class Levels:
    def __init__(self, levelData = []):
        self.levelData = levelData
    
    
    def getLevelData(self, level):
        for levelData in self.levelData:
            if levelData["level"] == level:
                return levelData["level"]
            
        
class FileBoundLevelsFactory:
    def create(self):
        encoder = JsonEncoder()
        decoder = JsonDecoder()
        cwd = os.getcwd()
        fileHandler = FileDataHandler(cwd + "\\data\\levels.json")
        return FileBoundLevels(fileHandler, decoder, encoder)


class FileBoundLevels(Levels, FileBound):
    def __init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy):
        Levels.__init__(self)
        FileBound.__init__(self, fileHandler, dataDecodingStrategy, dataEncodingStrategy)
    
    def toSerializable(self):
        pass
    
    def setData(self, data):
        self.levelData = data
    