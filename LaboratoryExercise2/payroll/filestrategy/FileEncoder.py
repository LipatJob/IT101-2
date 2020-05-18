class FileEncoder:
    """ Creates string that represents row-value data that is separated by a row delimiter and a value delimiter
    
    Example
    -------
    val = [['Hello', 'world'],['red', 'fox']]   # example list
    encoder = FileEncoder(',', ';')   # create Encoder with ',' as value delimiter and ';' as row delimiter
    print(encoder.encode(val))                  # prints 'Hello,world;red,fox;'
     
    """
    def __init__(self, valueDeliminator, rowDeliminator):
        self.valueDeliminator = valueDeliminator
        self.rowDeliminator = rowDeliminator
    
    def encode(self, data):
        return self.rowDeliminator.join([self.valueDeliminator.join([str(stringval) for stringval in val]) for val in data]) + self.rowDeliminator