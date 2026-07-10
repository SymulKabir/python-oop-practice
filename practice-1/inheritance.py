class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"My name is {self.name}, and salary is {self.salary}")
    
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
        
    def display(self):
        print(f"My name is {self.name}, salary is {self.salary} and language is {self.language}")
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        print(f"Name is {self.name}, salary is {self.salary}, department {self.department}")
        
        
dev = Developer("My kamal", 2000, "JS")
dev.display()

man = Manager("Mr Jalal", 400, "Store")

man.display()