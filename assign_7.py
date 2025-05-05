#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:

#a public variable name,

#a protected variable _age, and

#a private variable __salary.

#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,my_name,my_age,my_salary):
        self.name=my_name
        self._age=my_age
        self.__salary=my_salary

E1=Employee("Donia",35,12345)
print(E1.name)
print(E1._age) # This is a protected attribute and we can access it directly outside the
#class but it is not recommended to access the protected attribute outside the class. 
#The best way to access a protected attribute is to access them in the derived class 
#through a public method and then call that method with that class's object or you can use it in a public method within the class 
# where this protected attribute has been defined and then call that public method with the 
#help of that class's object

#print(E1.__salary)
#This is a private attribute and you cannot access or modify it directly outside the class where it has
#been defined or in the derived class.You can access and modify the private attribute only within the class through public methods
# iF YOU WANT TO ACCESS AND MODIFY THE PRIVATE ATTRIBUTE OUTSIDE THE CLASS :A mechanism called 
# NAME MANGLING is used . 

# Exmple of NAME MANGLING  ----- to check the result comment out line number 28
print(E1._Employee__salary)
E1._Employee__salary=5678
print(E1._Employee__salary)