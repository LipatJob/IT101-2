class CityEntity:
    def __init__(self, cityName = "", brgyData = {}):
        self.cityName = cityName
        self.barangays = brgyData
    
    def resetBarangay(self):
        self.barangays = {}
    
    def addBarangay(self, barangay):
        self.barangays[barangay[0]] = barangay[1]
        
    def deleteBarangay(self, barangayName):
        if barangayName in self.barangays:
            del self.barangays[barangayName]
        else:
            raise ValueError
    
    def editBarangay(self, barangayName, data):
        self.barangays[barangayName] = data
    
    def getBarangays(self):
        return set(self.barangays)
    
    def getBarangay(self, barangayName):
        return self.barangays[barangayName]
    
    