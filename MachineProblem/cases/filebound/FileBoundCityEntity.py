from cases.entities.CityEntity import CityEntity
from cases.filebound.FileBound import FileBound

class FileBoundCityEntity(FileBound, CityEntity):
    def __init__(self, cityName, fileHandler, dataParsingStrategy, dataEncodingStrategy):
        CityEntity.__init__(self, cityName, {})
        FileBound.__init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy)
    
    def toSerializable(self):
        """ Convert data into array """
        arr = [['BRGY', 'CONFIRMED', 'ACTIVE', 'RECOVERED', 'SUSPECT', 'PROBABLE', 'DECEASED']]
        for key, val in self.barangays.items():
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
        self.resetBarangay()
        for row in data[1:]:
            brgy = row[0]
            Confirmed = int(row[1])
            Active = int(row[2])
            Recovered = int(row[3])
            Suspect = int(row[4])
            Probable = int(row[5])
            Deceased = int(row[6])
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
            self.addBarangay(val)
        
        