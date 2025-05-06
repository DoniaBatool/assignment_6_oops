#20. Creating a Custom Exception
#Assignment:
#Create a custom exception InvalidAgeError. Write a function check_age(age) that 
#raises this exception if age < 18. Handle it with try...except.

# 1. Custom exception define
class InvalidAgeError(Exception):
    """Uthai jaata hai jab age < 18 ho."""
    pass

# 2. Function jo age check kare
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be at least 18.")
    print("Age valid. Access granted.")

# 3. Try…except mein istemal
if __name__ == "__main__":
    try:
        user_age = int(input("Apni age batao: "))
        check_age(user_age)
    except InvalidAgeError as e:
        print("Error:", e)
    except ValueError:
        print("Please ek valid number enter karo.")
    else:
        print("Welcome!")
