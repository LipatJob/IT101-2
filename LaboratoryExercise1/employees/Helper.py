def inputNumber(message = "", errorMessage = "Please Enter A Valid Number", comparator = lambda x: True):
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
            

def inputComparator(message = "", errorMessage = "Please Enter Valid Value", comparator = lambda x: True, force_lower = False):
    while True:
        inputValue = input(message)
        if force_lower:
            inputValue = inputValue.lower()
        try:
            if comparator(inputValue):
                return inputValue
            else:
                raise ValueError
            break
        except ValueError:
            print(errorMessage + ".", "Input Value:", inputValue)
            
            
def notblank(value):
    if len(value) == 0:
        return False
    return not value.isspace()