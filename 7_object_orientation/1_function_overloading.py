#polymorphism=method overloading and file overloading(doing in one project diferent forms is called ---)
class function_overloading:
    def add(self,a,b):
        self.res1=a+b
        print('add {0} and {1} is {2}'.format(a,b,self.res1))
    def add(self,a,b,c):
        self.res2=a+b+c
        print('add {0},{1} and {2} is {3}' .format(a,b,c,self.res2))
print("function overloading demo")
print("enter 3 int num:")
n1=int(input())
n2=int(input())
n3=int(input())
fobj=function_overloading()
fobj.add(n1,n2,n3)
#fobj.add(n1,n2)
#note: id doesn't support function overloading