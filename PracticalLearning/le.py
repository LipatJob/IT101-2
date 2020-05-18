#VVVVVVVVVVV



#^^^^^^^^^^^

#VVVVVVVVVVV



#^^^^^^^^^^^
data = 50
try:
    data = data/10
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("GFG")
# else:
#     print("Division Successful")
#VVVVVVVVVVV

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print("after f?")
a()

#^^^^^^^^^^^




#VVVVVVVVVVV

data = 50

try:
    data = data / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("division successful")
    
    
try:
    data = data / 5
except:
    print("insider except blck")
else:
    print("GFG")

#^^^^^^^^^^^



#VVVVVVVVVVV


def foo():
    try:
        print(1)
    finally:
        print(2)

#^^^^^^^^^^^

#VVVVVVVVVVV

try:
    print(1)
    # Do something

except:
    print(1)
    # Do something

else:
    print(1)
    # Do something

#^^^^^^^^^^^

#VVVVVVVVVVV

try:
    print(1)
    # Do something

except:
    print(1)
    # Do something

finally:
    print(1)
    # Do something

#^^^^^^^^^^^

#VVVVVVVVVVV

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
    

#^^^^^^^^^^^


#VVVVVVVVVVV


value  = [1, 2, 3, 4]
data = 0
try:
    data = value[3]
except IndexError:
    print("GFG IndexError")
except:
    print("Hello")
finally:
    print("Geeks IndexError")

data = 10
try:
   data = data/0
except ZeroDivisionError:
    print("GFG ZeroDivisionError")
finally:
    print("geeks ZeroDivisionError")


#^^^^^^^^^^^