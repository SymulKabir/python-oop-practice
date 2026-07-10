from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    @abstractclassmethod
    def start(self):
        pass
    
    @abstractclassmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def __init__(self):
        pass
    def start(self):
        print("Car is starting...")
        
    def stop(self):
        print("Stop car ....")
        
class Bike(Vehicle):

    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")
my_can = Car()

my_can.start()
my_can.stop()


my_bike = Bike()

my_bike.start()
my_bike.stop()