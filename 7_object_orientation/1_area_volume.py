#area=l*b
#volume=l*b*h
class areavol:
    def area(self):
        l=12
        b=13
        area=l*b
        print("res of area:",area)
    def vol(self):
        l=12
        b=13
        h=14
        vol=l*b*h
        print("res of vol:",vol)
print("addition program using object orientation")
aobj=areavol()
aobj.area()
aobj.vol()
