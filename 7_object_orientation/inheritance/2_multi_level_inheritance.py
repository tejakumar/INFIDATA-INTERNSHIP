class A:
    def __init__(self,n1,n2):
        self.a=n1
        self.b=n2
    def add(self):
        self.sum=self.a+self.b
        print("sum is:", self.sum)

class B(A):
    def __init__(self,n1,n2):
            super().__init__(n1,n2)  # to invoke base class constructer

    def sub(self):  # inhertance
            self.sub = self.a-self.b
            print("sub is:", self.sub)
class C(B):
    def __init__(self,n1,n2,n3):
         super().__init__(n1,n2)
         self.c=n3
    def mul(self):
         self.mul=self.a*self.b*self.c
         print("mul is:",self.mul)

print("enter 3 int number:")
x= int(input())
y= int(input())
z= int(input())
cobj = C(x,y,z)
cobj.add()  # inhertance
cobj.sub()
cobj.mul()