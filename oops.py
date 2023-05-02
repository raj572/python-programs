# class Myclass:
#     number=25
#     fnumber=2.5
#     string='OOP'
#     li=[1,5,2,8,6,3]
#     tp=(1,5,2,6)
#     st={1,2,5,8,6}
#     dt={4:25,5:98}
# myobj=Myclass()
# print(myobj.dt)


'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Mammal(Animal):
    def __init__(self, name, species, diet):
        super().__init__(name, species)
        self.diet = diet

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name, species, habitat):
        super().__init__(name, species)
        self.habitat = habitat

class Lion(Mammal):
    def __init__(self, name):
        super().__init__(name, 'Lion', 'Carnivore')

    def roar(self):
        print("ROAR!")

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name, 'Penguin', 1.5)

    def swim(self):
        print("Swimming...")

class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name, 'Snake', 'Desert')

    def slither(self):
        print("Slithering...")

class Crocodile(Reptile):
    def __init__(self, name):
        super().__init__(name, 'Crocodile', 'Swamp')

    def swim(self):
        print("Swimming...")

lion = Lion('Simba')
lion.roar()

penguin = Penguin('Tux')
penguin.swim()

snake = Snake('Kaa')
snake.slither()

crocodile = Crocodile('Snappy')
crocodile.swim()
'''
# class Person:
#     def __init__(self, name="Unknown", age=0):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         print(f"{self.name} is {self.age} years old.")

# person1 = Person(input("Enter first person name : "),int(input("Enter his age: ")))
# person2 = Person(input("Enter second person name : "),int(input("Enter his age: ")))
# person1.get_info()  # Alice is 25 years old.
# person2.get_info()  # Unknown is 0 years old.

'''

class Book:
    def __init__(self, title, author, isbn, year_published, num_pages, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published
        self.num_pages = num_pages
        self.genre = genre
class Library:
    def __init__(self):
        self.inventory = []

    def add_book(self, book):
        self.inventory.append(book)

    def remove_book(self, isbn):
        for book in self.inventory:
            if book.isbn == isbn:
                self.inventory.remove(book)
                return True
        return False

    def search_book(self, isbn):
        for book in self.inventory:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        for book in self.inventory:
            print(book.title)
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803", 1979, 193, "Science Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960, 281, "Historical Fiction")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.list_books()  
library.remove_book("9780345391803")
library.list_books()
'''
# Define the Book class
class Book:
    def __init__(self, title, author, isbn, year_published, num_pages, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published
        self.num_pages = num_pages
        self.genre = genre

# Define the Library class
class Library:
    def __init__(self):
        self.inventory = []

    def add_book(self, book):
        self.inventory.append(book)

    def remove_book(self, isbn):
        for book in self.inventory:
            if book.isbn == isbn:
                self.inventory.remove(book)
                return True
        return False

    def search_book(self, isbn):
        for book in self.inventory:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        for book in self.inventory:
            print(book.title)

# Create an empty Library object
library = Library()

# Allow the user to add books to the library
while True:
    # Prompt the user for book information
    title = input("Enter the book's title (or 'quit' to exit): ")
    if title == 'quit':
        break
    author = input("Enter the author's name: ")
    isbn = input("Enter the book's ISBN: ")
    year_published = int(input("Enter the year the book was published: "))
    num_pages = int(input("Enter the number of pages in the book: "))
    genre = input("Enter the book's genre: ")

    # Create a Book object and add it to the library's inventory
    book = Book(title, author, isbn, year_published, num_pages, genre)
    library.add_book(book)

# List all the books in the Library's inventory
library.list_books()
