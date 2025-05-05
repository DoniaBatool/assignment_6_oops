#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. 
#Add a class method change_bank_name(cls, name) that allows changing the bank name.
#Show that it affects all instances.

class Bank:
    bank_name="Bank Al Habib"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name
        return cls.bank_name

bank1=Bank()
print(bank1.change_bank_name("Meezan Bank"))

bank2=Bank()
print(bank2.change_bank_name("JS Bank"))








