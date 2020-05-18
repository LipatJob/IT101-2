"""
# 2.
# print(x) #This statement will raise an error because x is not defined

# 3.
# The try block will generate an exception, because x is not defined
try:
    print(x)
except:
    print("An exception occured")
    
# 4.
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    
# 5.
# Else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
""" 

# Finally
try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished") # Execute regardless if try block raises an error or not
