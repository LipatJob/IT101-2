class A:
    def test(self):
        print("test of A called")
class B(A): 
    def test(self):
        print("test of B called")
        super().test()
class C(A): 
    def test(self):
        print("test of C called")
        super().test()
class D(B, C): 
    def test2(self):
        print()

obj = D()
obj.test()

print()
print()
print()

class Sales:
    def __init__(self, id):
        self.id = id
        id = 100
val = Sales(123)
print(val.id)

print()
print()
print()

class Person:
    def __init__(self, id):
        self.id = id
        
sam = Person(100)
sam.__dict__['age'] = 49
print(sam.age + len(sam.__dict__))

print()
print()
print()


class fruits:
    def __init__(self):
        self.price = 100
        self.__bags = 5
    def display(self):
        print(self.__bags)
obj = fruits()
obj.display()


print()
print()
print()

s = "\t\tWelcome\n"
print(s.strip())
    
# print()
# print()
# print()

# class A:
#     def __init__(self, i = 0):
#         self.i = i

# class B(A):
#     def __init__(self, j = 0):
#         self.j = j
        
# def main():
#     b = B()
#     print(b.i)
#     print(b.j)
    
# main()


class A:
    def __init__(self):
        self.calcI(30)
        print("I from A is", self.i)
    
    def calcI(self, i):
        self.i = 2 * i
        
class B(A):
    def __init__(self):
        super().__init__()
    
    def calcI(self, i):
        self.i = 3 * i
b = B()

print()
print()
print()


    
print()
print()
print()
    