#18. Property Decorators: @property, @setter, and @deleter
#Assignment:
#Create a class Product with a private attribute _price. 
#Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        # Private attribute
        self._price = price

    @property
    def price(self):
        """Getter: price ko read-only attribute ki tarah return kare."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Setter: price ko update kare. Yahan validation bhi daal sakte hain."""
        if new_price < 0:
            raise ValueError("Price negative nahin ho sakta!")
        self._price = new_price

    @price.deleter
    def price(self):
        """Deleter: price attribute ko delete kare."""
        print("Deleting price…")
        del self._price


# Usage example
p = Product(100)
print(p.price)     # Getter chaleyga, output: 100

p.price = 150     # Setter chaleyga, price update hogaya
print(p.price)     # Output: 150

del p.price       # Deleter chaleyga, prints "Deleting price…"
# ab p._price attribute nahi raha
