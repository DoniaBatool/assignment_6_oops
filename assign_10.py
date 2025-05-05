#10. Instance Methods
#Assignment:
#Create a class Dog with instance variables name and breed. 
#Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self,name):
        self.name=name
        self.breed="German Shephered"
    def Bark(self):                    
        print(f"The dog named {self.name} barked woof woof at the pedestrians")

D1 = Dog("Floppy")
print(D1.breed)
D1.Bark()

