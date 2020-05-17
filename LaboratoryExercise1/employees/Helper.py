def inputNumber(message = "", errorMessage = "Please Enter A Valid Number", comparator = lambda x: True):
    """" Lets user input an integer """
    while True:
        inputValue = input(message)
        try:
            inputValue = int(inputValue)
            if comparator(inputValue):
                return inputValue
            else:
                raise ValueError
            break
        except ValueError:
            print(errorMessage, "Input Value:", inputValue)
            

def inputComparator(message = "", errorMessage = "Please Enter Valid Value", comparator = lambda x: True, force_lower = False, strip = False):
    """ Lets user input a valid string that is validated by a comparator """
    while True:
        inputValue = input(message)
        if force_lower:
            inputValue = inputValue.lower()
        if strip:
            inputValue = inputValue.strip()
        try:
            if comparator(inputValue):
                return inputValue
            else:
                raise ValueError
            break
        except ValueError:
            print(errorMessage, "Input Value:", inputValue)
            
            
def notblank(value):
    """ Returns whether the argument is a blank string or a whitespace """
    if len(value) == 0:
        return False
    return not value.isspace()

def getAge(currentDate, birthDate):
    """ Returns the age in years """
    age = currentDate.year - birthDate.year - 1
    
    if currentDate.month > birthDate.month:
        age += 1
        
    if currentDate.month == birthDate.month and currentDate.day >= birthDate.day:
        age += 1
        
    return age