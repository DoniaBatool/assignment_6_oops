#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object
# to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine starts")
    def __del__(self):
        print("The Engine object has been destroyed")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car owns the Engine

    def drive(self):
        self.engine.start()
        print("The car is moving")
    def __del__(self):
        print("The car object has been destroyed")

my_car = Car()
my_car.drive()
del my_car
#print(my_car)
E1 = Engine()# ye dusra object hai aur wo object jo car class k ander hai wo different 
            #hai dono ka apus mae koi lena dena nai hai . comment out line number 24 to see the results
E1.start()


