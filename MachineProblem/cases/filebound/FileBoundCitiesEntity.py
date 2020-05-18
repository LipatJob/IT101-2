from cases.entities.CityEntity import CityEntity
from cases.entities.CitiesEntity import CitiesEntity
from cases.entities.filebound.FileBound import FileBound

class FileBoundCitiesEntity(CitiesEntity, FileBound):
    def __init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy, cityFactory):
        CitiesEntity.__init__(self)
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
        self.cityFactory = cityFactory
        
    def toSerializable(self):
        """ Convert data into json """
        json = {"cities" : []}
        for city in super._cities:
            location = city.cityName.replace(" ", "") + "Cases"
            cityData = [city.cityName, location]
            json["cities"].append(cityData)
        return json
    

    def setData(self, data):
        """ Set data from array """
        super().resetCities()
        for row in data["cities"]:
            cityName = row[0]
            fileLocation = row[1]
            super().addCity(cityFactory.create(cityName, fileLocation))
    

        
    
    