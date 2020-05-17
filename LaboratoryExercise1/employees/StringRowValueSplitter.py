class StringRowValueSplitter:
    """Splits a string that contains data that is seprated by a row delimiter and a value delimiter
    
    Example
    -------
    text = "hello,world;red,fox;"               # setup text 
    splitter = StringRowValueSplitter(',', ';') # instantiate objecct
    return splitter.parse(text)                 # returns [['hello','world'],['red','fox']]
    
    """
    def __init__(self, valueDeliminator, rowDeliminator):
        self.valueDeliminator = valueDeliminator
        self.rowDeliminator = rowDeliminator
        
    def parse(self, string: str):
        return [[cell.strip() for cell in row.split(self.valueDeliminator)] for row in string.split(self.rowDeliminator)]