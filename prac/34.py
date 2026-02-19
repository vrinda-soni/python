#Build a small library system with Book, Member, and Library classes. Library supports add_book(), borrow_book(member), return_book(member), and list_available(). Demonstrate all operations.
class book():
    def __init__(self , title): 
        self.title = "ikigai"
        self.available = True

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} title"
    
class member():
    def __init__(self,name):
        self.name = "abc"

    def __str__ (self):
        return self.name
    
class library():
    def __init__(self):
        self.books=[]
        self.borrowed={}

    #for adding book
    def add_book(self,book):
        self.book.append(book)

    #for borrowing book
    def borrow_book(self,member,title):
        for book in self.books:
            if book.title==title and book.available:
                book.available = False
                self.borrowed.setdefault(member.name,[]).append(title)
                return "borrowed!"
            
        return "books not available"
    
    #return book 
    def return_book(self, member,title):
        if member.name in self.borrowed and title in self.borrowed[member.name]:
            self.borrowed[member.name].remove(title)
            for book in self.books:
                if book.title==title:
                    book.available = True
                return "returned!"
        return "invalid return"
    
    #list available
    def available(self):
        return [str(book)for book in self.books if book.available]
    
