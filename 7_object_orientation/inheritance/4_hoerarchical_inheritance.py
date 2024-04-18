class A:
    def __init__(self,n1,n2):
        self.a=n1
        self.b=n2

    def add(self):
        self.add = self.a + self.b
        print('add is:', self.add)

class B(A):
    def __init__(self,n1,n2):
        super().__init__(n1,n2)#super keyword is used to involue the base class constructor

    def sub(self):
        self.sub = self.a - self.b
        print('sub is:', self.sub)


class C(A):
    def __init__(self,n1,n2):
        super()._init_(n1,n2)#super keyword is used to involue the base class constructor

    def mul(self):
        self.mul = self.a * self.b
        print('mul is:', self.mul)


print("from B to A Class:")
x=int(input("enter num1:"))
y=int(input("enter num2:"))
bobj = B(x,y)
bobj.add()  #inheritance
bobj.sub()

print("from c to A Class:")
x=int(input("enter num1:"))
y=int(input("enter num2:"))
cobj = C(x,y)
cobj.add()  #inheritance
cobj.mul()

