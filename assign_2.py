#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. 
#Use a class variable and a class method with cls to manage and display the count.

class Counter:
    obj_counter=1 

    @classmethod
    def my_counter(cls,new_value):
        cls.obj_counter+=new_value
        return cls.obj_counter


c1=Counter()
print(c1.my_counter(2))
