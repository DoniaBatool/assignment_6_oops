#8. The super() Function
#Assignment:
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it,
# add a subject field, and use super() to call the base class constructor.
class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        #Person.__init__(self,name)
        self.subject=subject
       
T1= Teacher("Miss Sara","Maths")
print(T1.name)
print(T1.subject)