class A1:
    def __init__(self,a,b):
        self.l=a
        self.b=b
    def area(self):
        self.area=self.l * self.b
        print("area is:",self.area)
class B1(A1):
    def __init__(self,a,b,c):
        super(). __init__(a,b)    #to invoke base class constructer
        self.h=c
    def volume(self):  #inhertance
        self.vol=self.l*self.b*self.h
        print("volume is:",self.vol)

print("area volume program")
print("enter l,b & h values")
l1=int(input())
b1=int(input())
h1=int(input())
bobj=B1(l1,b1,h1)
bobj.area()  #inhertance
bobj.volume()