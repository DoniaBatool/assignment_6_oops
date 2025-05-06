
#19. callable() and __call__()
#Assignment:
#Create a class Multiplier with an __init__() to set a factor. 
#Define a __call__() method that multiplies an input by the factor. 
#Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self):
        print("I am the contructor and i will multiply the input by 24")
        self.factor = 24
    def __call__(self,num):
        print("I an callable ---- the dunder method")
        result= self.factor*num
        return print(f"The result is : {result}")
    
M1 = Multiplier()
print(callable(M1))
M1(4)
