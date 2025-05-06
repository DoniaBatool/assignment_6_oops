#16. Function Decorators
#Assignment:
#Write a decorator function log_function_call that prints "Function is being called" 
#before a function executes. Apply it to a function say_hello().


def log_function_call(func):
    def wrapper():    
        print("The Function is being called")
        func()
        print("After the Function has been called")
    return wrapper    

@log_function_call
def say_hello():
    print("Hello from the decorator function")
    

say_hello()


# 1. Decorator define
def log_function_call(func):
    def wrapper(*args, **kwargs):
        # args aur kwargs dono print kar rahe
        print(f"Function '{func.__name__}' is being called")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        func("ahmed",greeting="salam")
        return func
    return wrapper

# 2. Decorator apply
@log_function_call
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# 3. Function calls with args aur kwargs
#greet("Donia")
# Output:
# Function 'greet' is being called
#   args: ('Donia',)
#   kwargs: {}
# Hello, Donia!

greet("Ali", greeting="Hi")
# Output:
# Function 'greet' is being called
#   args: ('Ali',)
#   kwargs: {'greeting': 'Hi'}
# Hi, Ali!
