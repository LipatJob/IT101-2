"""
# 2
class Player(object):
    def __init__(self, name = "Enterprise", fuel = 0):
        self.name = name
        self.fuel = fuel
    
    def status(self):
        print(self.name, self.fuel)

myship = Player("Apollo")
myship.status()
"""

"""
# 4
class Animal(object):
    def __init__(self, name):   #Constructor
        self.name = name
    
    def get_name(self):
        return self.name
    
class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'), Cat('Mr. Bojangles'), Dog('Lassie')]

for animal in animals:
    print(animal.talk() + " I am " + animal.get_name())
    
"""

# 6
class Animal(object):
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        return 'Hello'
    
class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Fish(Animal):
    pass

yourPet = Animal('Zoro')
print(yourPet.talk())

myPet = Cat('Mingming')
print(myPet.talk())

hisPet = Fish('Ariel')
print(hisPet.talk())