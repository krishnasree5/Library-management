
#Creating a class:- Genre
class Genre():
    def __init__(self, genre_name):
        self.genre_name = genre_name
        self.books = []
    
    def add_books(self, *books):
        for book in books:
            self.books.append(book)
    
    def print_books(self):                              #function to print all books in a given Genre
        print("All books in",self.genre_name,"are")
        for book in self.books:
            print("ID: ",book.ID)
            print("Name: ",book.name)
            print("Author: ",book.author)
            print("Genre: ",book.genre_name)
            print("Stock Left: ",book.stock)
       

#Creating Book class which is a child of Genre class
class Book(Genre):
    def __init__(self, ID, name, author, genre_name, stock):
        super().__init__(genre_name)
        self.ID = ID
        self.name = name
        self.author = author
        self.stock = stock
    
    def print_book(self):                               #function to print a book
        print("ID: ",self.ID)
        print("Name: ",self.name)
        print("Author: ",self.author)
        print("Genre: ",self.genre_name)
        print("Stock Left: ",self.stock)


#Creating instances of Genre
Mathematics = Genre("Mathematics")
Science = Genre("Science")
Biography = Genre("Biography")
Novels = Genre("Novels")
Science_Fiction = Genre("Science Fiction")
genre_list = [Mathematics, Science, Biography, Novels, Science_Fiction]         


#Creatind each book as an instance of Book class
Basic_Maths_For_Dummies = Book(1, "Basic Maths For Dummies", "Colin Beveridge", "Mathematics", 20)
Higher_Engineering_Mathematics = Book(2, "Higher Engineering Mathematics", "B.S Grewal", "Mathematics", 18)
The_Elements_of_Coordinate_Geometry = Book(3, "The Elements of Coordinate Geometry", "S.L. Loney",
                                            "Mathematics", 32)
The_Art_of_Statistics_How_to_Learn_from_Data = Book(4, "The Art of Statistics: How to Learn from Data",
                                                     "David Spiegelhalte", "Mathematics", 10)
Calculus_Made_Easy = Book(5, "Calculus Made Easy", "Silvanus P. Thompson", "Mathematics", 24)


A_Brief_History_of_Time = Book(11, "A Brief History of Time", "Stephan Hawking", "Science", 13)
On_the_Origin_of_Species = Book(12, "On the Origin of Species", "Charles Darwin", "Science", 45)
The_Immortal_Life_of_Henrietta_Lacks = Book(13, "The Immortal Life of Henrietta Lacks", "Rebecca Skloot",
                                             "Science", 54)
Silent_Spring = Book(14, "Silent Spring", "Rachel Carson", "Science", 29)
A_Short_History_of_Nearly_Everything = Book(15, "A Short History of Nearly Everything", "Bill Bryson",
                                             "Science", 56)


Alan_Turing_The_Enigma = Book(21, "Alan Turing: The Enigma", "Andrew Hodges", "Biography", 8)
Steve_Jobs = Book(22, "Steve Jobs", "Walter Isaacson", "Biography", 13)
Frida = Book(23, "Frida", "Hayden Herrera", "Biography", 45)
A_Beautiful_Mind = Book(24, "A Beautiful Mind", "Sylvia Nasar", "Biography", 65)
My_Inventions_The_Autobiography_of_Nikola_Tesla = Book(25, "My Inventions - The Autobiography of Nikola Tesla"
                                                       , "Ben Johnston", "Biography", 32)


The_Great_Gatsby = Book(31, "The Great Gatsby", "F. Scott Fitzgerald", "Novels", 23)
Jane_Eyre = Book(32, "Jane Eyre", "Charlotte Brontë", "Novels", 27)
To_Kill_a_Mockingbird = Book(33, "To Kill a Mockingbird", " Harper Lee", "Novels", 31)
Metamorphosis = Book(34, "Metamorphosis", "Franz Kafka", "Novels", 52)
Crime_and_Punishment = Book(35, "Crime and Punishment", "Fyodor Dostoevsky", "Novels", 1)


Dune = Book(41, "Dune", "Frank Herbert", "Science Fiction", 2)
The_Hitchhikers_Guide_to_the_Galaxy = Book(42, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams",
                                            "Science Fiction", 8)
Frankenstein = Book(43, "Frankenstein", "Mary Shelly", "Science Fiction", 35)
The_Three_Body_Problem = Book(44, "The Three-Body Problem", "Liu Cixin", "Science Fiction", 42)
The_Martian = Book(45, "The Martian", "Andy Weir", "Science Fiction", 27)


#Adding books to each Genre
Mathematics.add_books(Basic_Maths_For_Dummies, Higher_Engineering_Mathematics, The_Elements_of_Coordinate_Geometry
                      , The_Art_of_Statistics_How_to_Learn_from_Data, Calculus_Made_Easy)

Science.add_books(A_Brief_History_of_Time, On_the_Origin_of_Species, The_Immortal_Life_of_Henrietta_Lacks,
                   Silent_Spring, A_Short_History_of_Nearly_Everything)

Biography.add_books(Alan_Turing_The_Enigma, Steve_Jobs, Frida, A_Beautiful_Mind,
                     My_Inventions_The_Autobiography_of_Nikola_Tesla)

Novels.add_books(The_Great_Gatsby, Jane_Eyre, To_Kill_a_Mockingbird, Metamorphosis, Crime_and_Punishment)

Science_Fiction.add_books(Dune, The_Hitchhikers_Guide_to_the_Galaxy, Frankenstein, The_Three_Body_Problem
                          , The_Martian)


#view books genrewise
def view_by_genre():        
    genre_name = input("Name of the genre: ")
    for genre in genre_list:
        if genre_name.lower() == genre.genre_name.lower():
            genre.print_books()
            break
    
#view books based on user inputs (name or id)
def view_book_by_ID():
    book_num = int(input("ID of the given book: "))
    for genre in genre_list:
        for book in genre.books:
            if book.num == book_num:
                book.print_book()
                break

def view_book_by_name():
    book_name = input("Name of the given book: ")
    for genre in genre_list:
        for book in genre.books:
            if book.name.lower() == book_name.lower():
                book.print_book()
#edge cases in all three: book not found


# function to create book
def create_book():
    genre_name = input("Enter name of genre: ")
    print("Enter book details: ")
    book_name = input("Name: ")
    book_author = input("Author: ")
    num = input("Enter ID: ")                           #edge case: id alredy existing
    stock = int(input("Enter stock: "))
    obj2 = Book(num, book_name, book_author, genre_name, stock)
    for i in genre_list:
        if i.genre_name.lower() == genre_name.lower():
            i.add_books(obj2) 
    else:
        obj1 = Genre(genre_name)
        genre_list.append(obj1)
        obj1.add_books(obj2)


'''To do:
delete book
librarian interface(create, delete, view stock, view who issued what)
user interface(login, create, dashboard, issue books)
main function'''