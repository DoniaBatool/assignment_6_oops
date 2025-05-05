#11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. 
#Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    
    total_books = 10
    book_list = []

    @classmethod
    def increment_book_count(cls, book):
        cls.book_list.extend(book)  
        cls.total_books += len(cls.book_list)      
        print(f"The total books are {cls.total_books}")

        
B1 = Book()
B1.increment_book_count(["HARRY POTTER","Cook Book","Cocktail"])
print(B1.total_books)
print(B1.book_list)



