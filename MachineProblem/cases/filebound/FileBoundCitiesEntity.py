from cases.entities.CityEntity import CityEntity
from cases.entities.CitiesEntity import CitiesEntity
from cases.filebound.FileBound import FileBound

class FileBoundCitiesEntity(CitiesEntity, FileBound):
    def __init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy, cityFactory):
        CitiesEntity.__init__(self)
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
        self.cityFactory = cityFactory
        
    def toSerializable(self):
        """ Convert data into json """
        json = {"cities" : []}
        for city in self._cities:
            location = city.cityName.replace(" ", "") + "Case.txt"
            cityData = [city.cityName, location]
            json["cities"].append(cityData)
        return json
    

    def setData(self, data):
        """ Set data from array """
        self.resetCities()
        for row in data["cities"]:
            cityName = row[0]
            fileLocation = row[1]
            city = self.cityFactory.create(cityName, fileLocation)
            city.retrieveState()
            self.addCity(city)
    

        
    
    