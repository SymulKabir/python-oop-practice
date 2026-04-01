class Person:
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    def get_info(self):
        return f"Name is {self.name} and age is {self.age}"
    


person_one = Person("Asis", 23)

person_one_info = person_one.get_info()

print(person_one_info)