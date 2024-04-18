class A:
    def __init__(self,a,b):
        self.l=a
        self.b=b
    def area(self):
        self.area=self.l * self.b
class B:
    def __init__(self,a,b,c):
        self.l=a
        self.b=b
        self.h=c
    def volume(self):
        self.volume=self.l*self.b*self.h
class C(A,B):
    def __init__(self,x,y,z):
        A.__init__(self,x,y)
        B.__init__(self,x,y,z)
    def display(self):  #inhertance
        print("area is:",self.area)
        print("volume is:",self.volume)

print("enter l,b & h values")
l=int(input())
b=int(input())
h=int(input())
cobj=C(l,b,h)
cobj.area()  #inhertance
cobj.volume()
cobj.display()