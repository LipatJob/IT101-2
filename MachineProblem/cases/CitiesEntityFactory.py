from cases.filebound.FileBoundCityFactory import FileBoundCityEntityFactory
from cases.filebound.FileBoundCitiesEntity import FileBoundCitiesEntity
from lib.JsonEncoder import JsonEncoder
from lib.JsonDecoder import JsonDecoder
from data.FileDataHandler import FileDataHandler
import os

class CitiesEntityFactory:
    """ Factory class for PayrollEntityManager. Creates FileBoundEntities instead of normal entities """
    
    def create(self):
        cwd = os.getcwd()
        encoder = JsonEncoder()
        decoder = JsonDecoder()
        metadatafileHandler = FileDataHandler(cwd + "\\data\\metadata.json")
        factory = FileBoundCityEntityFactory()
        cities = FileBoundCitiesEntity(metadatafileHandler, decoder, encoder, factory)
        cities.retrieveState()
        
        return cities
        