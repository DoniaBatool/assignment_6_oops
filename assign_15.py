#15. Method Resolution Order (MRO) and Diamond Inheritance
#Assignment:
#Create four classes:

#A with a method show(),

#B and C that inherit from A and override show(),

#D that inherits from both B and C.

#Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("This is show method from A class")

class B(A):
    def show(self):
        print("This is show method from B class")

class C(A):
    def show(self):
        print("This is show method from C class")

class D(B,C):
    pass

D1 = D()
D1.show()
print(D.mro())