class CityEntity:
    def __init__(self, cityName = "", brgyData = {}):
        self.cityName = cityName
        self.barangay = brgyData
    
    def addBarangay(self, barangay):
        self.barangay[barangay[0]] = barangay[1]
        
    def deleteBarangay(self, barangayName):
        if barangayName in self.barangay:
            del self.barangay[barangayName]
        else:
            raise ValueError
    
    def getBarangays(self):
        return set(self.barangay.keys())
    