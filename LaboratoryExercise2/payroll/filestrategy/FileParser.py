class FileParser:
    """ Splits a string that contains data that is seprated by a row delimiter and a value delimiter and stores it in an array
    
    Example
    -------
    text = "hello,world;red,fox;"                # setup text 
    splitter = StringRowValueSplitter(',', ';') # instantiate objecct
    print(splitter.parse(text))                 # prints [['hello','world'],['red','fox']]
    
    """
    def __init__(self, valueDeliminator, rowDeliminator):
        self.valueDeliminator = valueDeliminator
        self.rowDeliminator = rowDeliminator
        
    def parse(self, string):
        return [[cell.strip() for cell in row.split(self.valueDeliminator)] for row in string[:-1].split(self.rowDeliminator)]