#class => Library
# Layers of abstraction => display available books, to lend a book, to add a book

# class => Customer
# Layers of abstraction => request for a book, return a book

class Library:
      def __init__(self, listOfBooks):
          self.availableBooks = listOfBooks

      def displayAvailableBook(self):
          print()
          print("Availbe Books")
          for book in self.availableBooks:
              print(book)
    
      def lendBook(self, requestedBook):
          if requestedBook in self.availableBooks:
             print("You have borrowed the books")
          else:
             print("Sorry, the book is not available")

      def addBook(self, returnedBook):
          self.availableBook.append(returnedBook)
          print("Thank you, you have retuned the book")
class Customer:
      def requestBook(self):
          print("Enter the name of the book need to borrow")
          self.book = input()
          return self.book

      def returnBook(self):
          print("Enter the name of the book you are returning")
          self.book = input()
          return self.book
library = Library(['ABC'], ['XYZ'], ['PQR'])
customer = Customer()

while True:
   print("Enter 1 to display the available books")
   print("Enter 2 to request a book")
   print("Enter 3 to return a book")
   print("Enter 4 to exit")

   userChoise - int(input())
   if userChoise is 1:
     library.displayAvailableBooks()
   elif userChoise is 2:
     requestedBook = customer.requestBook()
     library.lendBook(requestedBook)
   elif userChoise is 3:
     returnedBook = customer.returnBook()  
     library.addBook(returnedBook)
   elif userChoice is 4:
     quit()
