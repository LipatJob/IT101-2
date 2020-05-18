"""
# 3.
# Get the character at position 1
# (remember that the first character has the position 0)

a = "Hello, World!"
print(a[1])

# 4.
# Substring.
# Get the characters from position 2 to position 5 (not included):

print(a[2:5])

# 5.
# The strip() method removes any whitespace
# from the beginning or the end:

a  = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
"""
 
# 7.
# The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))
# The lower() method returns the string in lower case:
print(a.lower())
# The upper() method returns the string in upper case:
print(a.upper())
# The replace() method replaces a string with another string:
print(a.replace("H","J"))
# The split() method splits the string into substrings
# if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', ' World!']

# 8.
# Import the datetime module and display the current date
import datetime

x = datetime.datetime.now()
print(x)

# Return the year and name of weekday:
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%I:%M %p | %A, %m of %B, %Y")) # Try

# The datetime() class requires three parameters
# to create a date: year, month, day

x = datetime.datetime(2020, 5, 17)
print(x)

