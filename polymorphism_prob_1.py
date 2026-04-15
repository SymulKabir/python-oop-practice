class Animal:
    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age
        self.breed = breed
        
    def make_sound(self):
        return "Some sound"
        

class Dog(Animal): 
    def make_sound(self):
        return f"{self.name} says Woof!"
    
    
class Cat(Animal): 
    def make_sound(self):
        return f"{self.name} says Meow!"
    
my_dog = Dog("Buddy", 3, "Golden Retriever")
my_cat = Cat("Whiskers", 2, "Siamese")

print(my_dog.make_sound())
print(my_cat.make_sound())