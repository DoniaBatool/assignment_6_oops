#6. Constructors and Destructors
#Create a class Logger that prints a message when an object is created (constructor) 
#and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("The new object of Logger class has been created")

    
    def __del__(self):
            print(f"The object of Logger class has been deleted")

l1 = Logger()
del l1




