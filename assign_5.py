#5. Static Variables and Static Methods
#Assignment:
#Create a class MathUtils with a static method add(a, b) that returns the sum. 
#No class or instance variables should be used.

class MathUtils:

    @staticmethod
    def add(a, b):
        return a+b
    
c1=MathUtils()
print(c1.add(5,4))

c2=MathUtils()
print(c2.add(15,4))