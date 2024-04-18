import math

def calculate_circle_area(radius):
    if radius<0:
        return
    else:
        area=math.pi * radius**2
        return area
radius=int(input('enter the radius'))
area=calculate_circle_area(radius)
print('the area of a circle',area)
