# Create a class called Dog instance attributes for name and age. Include a method that calculate and prints the dog's age in dog years (1 human year is equal to 7 dog years).
# Also, include a method that simulates the dog barking by printing "Woof!" to the console. Finally, create an instance of the Dog class and call both methods to demonstrate their functionality.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
        
        return "Woof!"
        
    def cal_dog_years(self):
        dog_years = self.age * 7
        print(f"{self.name} is {dog_years} years old in dog years.")
        
        return dog_years
    
    
my_dog = Dog("Buddy", 5)

my_dog.bark()
my_dog.cal_dog_years()