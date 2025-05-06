#17. Class Decorators
#Assignment:
#Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    # 1. greet method define karo
    def greet(self):
        return "Hello from Decorator!"

    # 2. greet method ko class me attach karo
    cls.greet = greet

    # 3. modified class return karo
    return cls


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())  
# Output: Hello from Decorator!