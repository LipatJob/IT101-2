from lib.StringRowValueEncoder import StringRowValueEncoder
from lib.StringRowValueSplitter import StringRowValueSplitter
from data.FileDataHandler import FileDataHandler
from cases.entities.CityEntity import CityEntity
class FileBoundCityEntityFactory:
    def create(self, cityName, fileLocation):
        fileHandler = FileDataHandler(fileLocation)
        dataEncodingStrategy = StringRowValueEncoder(",","\n")
        dataParsingStrategy = StringRowValueSplitter(",","\n")
        return FileBoundCity(fileHandler, dataParsingStrategy, dataEncodingStrategy)