class car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class Toyota(car):    # Single Inheritance
    def __init__(self,name):
        self.name = name

class Lambohrghini(Toyota): # Multilevel Inheritance
    def __init__(self,type):
        self.type = type

car1 = Lambohrghini("Lambohrghini")
car1.start()