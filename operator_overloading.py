class Square:
      def __init__(self, side):
          self.side = side
   
      def __add__(squareOne, squareTwo):
          return((4 * squareOne.side) + (4* squareTwo.side))

squareOne = Square(5) 
squareTwo = Square(10)

print("Sum of sides of both the square are: ", squareOne + squareTwo)
#TypeError: unsupported operand type(s) for +: 'instance' and 'instance'
# in that case you special __add__ method


