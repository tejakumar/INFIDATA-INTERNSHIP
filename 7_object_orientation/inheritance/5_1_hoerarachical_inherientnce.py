class areaClass:
    def area(self, a, b=None, c=None, d=None):

        # when a and c are passed as arguments
        if a != None and b != None and a != b and a != c:
            print("Area of the triangle", (0.5 * a * b))

        # when a,b,c and d are passed as arguments
        elif (b != None and c != None and d != None and a == b and a == c):
            print("Area of the square", (a * c))

        elif (b == None and c == None and d == None):
            print("Enter more numbers")
        else:
            if (a == c):
                print("Area of the rectangle", (a * b))
            else:
                print("Area of the rectangle", (a * c))


obj = areaClass()
obj.area(19, 8, 77)  # Area of the triangle 76.0
obj.area(18, 18, 18, 18)  # Area of the square 324
obj.area(72, 38, 72, 38)  # Area of the rectangle 2736