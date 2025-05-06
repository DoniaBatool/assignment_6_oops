#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department
#object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # aggregation: reference to a Department object

    def display(self):
        print(f"Employee: {self.name}, Department: {self.department.name}")

# Objects bana rahe hain
dep_accounts = Department("Accounts")
emp_ali = Employee("Ali", dep_accounts)

emp_ali.display()  # Employee: Ali, Department: Accounts

# Dono independent hain
del emp_ali        # sirf Employee object delete hoga
print(dep_accounts.name)  # phir bhi "Accounts" print hoga


