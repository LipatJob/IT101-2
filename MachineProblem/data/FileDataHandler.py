class FileDataHandler:
    """ Encapsulates file reading and writing """
    def __init__(self, fileLocation):
        self._fileLocation = fileLocation
        
        
    def updateData(self, data):
        """ Updates value of file to data """
        with open(self._fileLocation, "w") as file:
            file.write(data)
            
            
    def readData(self):
        """ Reads data from the file """
        data = ""
        with open(self._fileLocation, "r") as file:
            data = file.read()
        return data