class CitiesEntity:
    def __init__(self, cities = []):
        self._cities = cities
    
    def resetCities(self):
        self._cities = []
        
    def addCity(self, city):
        self._cities.append(city)
        
    def getCities(self):
        return self._cities
    
    def getCity(self, cityName):
        for city in self._cities:
            if city.cityName == cityName:
                return city
        return None
    