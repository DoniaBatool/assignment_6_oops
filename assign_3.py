#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). 
#Instantiate the class and access both from outside the class.

class Car:
    def __init__(self,my_brand):
        self.brand=my_brand
    
    def start(self):
        print("To start the car use gear and race")

c1=Car("Toyota")
print(c1.brand)
c1.start()