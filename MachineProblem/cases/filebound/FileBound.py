from abc import ABC, abstractmethod

class FileBound(ABC):
    """ An abstract class that allows children classes to serialize and deserialize data """
    def __init__(self, fileHandler, dataParsingStrategy, dataEncodingStrategy):
        self.fileHandler = fileHandler
        self.dataEncodingStrategy = dataEncodingStrategy
        self.dataParsingStrategy = dataParsingStrategy
    
    
    def saveState(self):
        """ Write data of this object to the attached file """
        dataString = self.dataEncodingStrategy.encode(self.toArray())
        self.fileHandler.updateData(dataString)
        
        
    def retrieveState(self):
        """ Set data of this object from the attached file"""
        dataString = self.fileHandler.readData()
        dataArray = self.dataParsingStrategy.parse(dataString)
        self.setData(dataArray)
    
    @abstractmethod
    def toSerializable(self):
        """ Convert the data object into a datatype that can be serializable by the strategy """
        pass
    
    @abstractmethod
    def setData(self, data):
        """ Set values from data parameter into fields of this object """
        pass