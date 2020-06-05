from lib.StringRowValueEncoder import StringRowValueEncoder
from lib.StringRowValueDecoder import StringRowValueDecoder
from data.FileDataHandler import FileDataHandler
from cases.filebound.FileBoundCityEntity import FileBoundCityEntity
import os

class FileBoundCityEntityFactory:
    def create(self, cityName, fileLocation):
        cwd = os.getcwd()
        
        fileHandler = FileDataHandler(cwd + "\\data\\" + fileLocation)
        dataEncodingStrategy = StringRowValueEncoder(",","\n")
        dataDecodingStrategy = StringRowValueDecoder(",","\n")
        city = FileBoundCityEntity(cityName, fileHandler, dataDecodingStrategy, dataEncodingStrategy)
        return city