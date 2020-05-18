## Code to initialize and restart demofile.txt
def resetFile():
    default_text = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""
    f = open("demofile.txt", "w")
    f.write(default_text)
    f.close()
    
resetFile()

"""
# 10.
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a
# read() method for reading the contents of the file

f = open("demofile.txt", "r")
print(f.read())

# 11.
# Read only parts of the file
# By default the read() method returns the whole text,
# but you can also specify how many characters you want to return
f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines
# You can return one line by using the readline() method
f = open("demofile.txt", "r")
print(f.readline())

# By calling readline() two times, you can read
# the first two lines

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# 14.
# By looping through the lines of the file,
# you can read the whole file, line by line:

f = open("demofile.txt", "r")
for x in f:
    print(x)
    
    
    
## Write to an existing file

resetFile()
# 15.
f = open("demofile.txt", "a")
f.write("\nNow the file has one more line!")
f.close()
f = open("demofile.txt", "r")
print(f.read())
"""

resetFile()
# 16.
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile.txt", "r")
print(f.read())

