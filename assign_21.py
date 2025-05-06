#21. Make a Custom Class Iterable
#Assignment:
#Create a class Countdown that takes a start number. 
#Implement __iter__() and __next__() to make the object iterable 
# in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # Iterator banane ke liye khud ko return karo
        return self

    def __next__(self):
        # Jab tak current 0 se bara hai, value return karo aur decrement karo
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        # Jab countdown khatam ho jaye, iteration stop kar do
        raise StopIteration

# Usage example:
for num in Countdown(0):
    print(num)

