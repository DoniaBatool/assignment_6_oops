#12. Static Methods
#Assignment:
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that 
# returns the Fahrenheit value.

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        fahrenheit= (c*9/5)+32
        return (f"The temperature in Fahrenheit is {fahrenheit} F ")

T1=  TemperatureConverter()
print(T1.celsius_to_fahrenheit(25))  