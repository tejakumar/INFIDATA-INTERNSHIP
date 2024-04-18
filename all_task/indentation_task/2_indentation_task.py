class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
    def perimeter(self):
        return 4 * self.side_length
my_square = Square(int(input('enter the my_square:')))
print("Area:", my_square.area())
print("Perimeter:", my_square.perimeter())
