from abc import ABC, abstractmethod
class Animal(ABC):
 
    @abstractmethod
    def species(self):
        pass 

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)


from abc import ABC, abstractmethod
class Animal2(ABC):
 
    @abstractmethod
    def species(self):
        print("of animal 2")

class Dog2(Animal2):
    
    @property
    def species(self):
        return "Canine2"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)
a2 = Dog2()
print(a2.species)