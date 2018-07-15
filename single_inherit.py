class Apple:
      manufacturer = "Apple INC."
      contact = "www.apple.com"

      def contactDetails(self):
          print("To contact us please visit our website", self.contact)

class MacBook(Apple):
      def __init__(self):
          self.yearOfManufacture = "2000"
      def manufactureDetails(self):
          print("This Macbook was manufactured by {} in {}".format(self.manufacturer,self.yearOfManufacture))


apple = Apple()
macbook = MacBook()

macbook.manufactureDetails()

