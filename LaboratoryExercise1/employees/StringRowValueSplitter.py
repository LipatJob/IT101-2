class StringRowValueSplitter:
    """Splits a row-value 
    
    """
    def __init__(self, valueDeliminator, rowDeliminator):
        self.valueDeliminator = valueDeliminator
        self.rowDeliminator = rowDeliminator
        
    def parse(self, string: str):
        return [[cell.strip() for cell in row.split(self.valueDeliminator)] for row in string.split(self.rowDeliminator)]