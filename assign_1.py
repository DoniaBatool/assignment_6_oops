#1. Using self
#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword
#to initialize these values via a constructor. Add a method display() 
#that prints student details.

class Student:
    def __init__(self,my_name,my_marks):
        self.name=my_name
        self.marks=my_marks

    def display(self):
        print(f"My name is {self.name} and my marks are {self.marks}")

s1=Student("Donia",90)
print(s1.name)
print(s1.marks)
s1.display()
