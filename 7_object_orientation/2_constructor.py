class addition:
    a=0
    b=0
    def __init__(self):
     self.a=int(input("enter the num1:"))
     self.b=int(input("enter the num2:"))
    def add(self):
        self.res=self.a+self.b
        print("add of{0} & {1} is {2}".format(self.a,self.b,self.res))
print("addition program")
aobj=addition()
aobj.add()
print("a value:",aobj.a)
print("b value:",aobj.b)
