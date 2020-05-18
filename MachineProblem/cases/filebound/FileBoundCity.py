from cases.entities.CityEntity import CityEntity
from cases.entities.filebound.FileBound import FileBound

class FileBoundCity(FileBound, CityEntity):
    def __init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy):
        CityEntity.__init__(self)
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
    
    def toSerializable(self):
        """ Convert data into array """
        arr = []
        for key, val in super().barangays:
            tempArr = []
            tempArr.append(key)
            tempArr.append(val["Confirmed"])
            tempArr.append(val["Active"])
            tempArr.append(val["Recovered"])
            tempArr.append(val["Suspect"])
            tempArr.append(val["Probable"])
            tempArr.append(val["Deceased"])
            arr.append(tempArr)
        return arr  
    
    
    def setData(self, data):
        """ Set data from array """
       # super().resetEmployees()
        for row in data:
            val = (
                brgy, {
                    "Confirmed" : Confirmed,
                    "Active" : Active,
                    "Recovered" : Recovered,
                    "Suspect" : Suspect,
                    "Probable" : Probable,
                    "Deceased" : Deceased
                }
            )
            super().addBarangay(val)
        