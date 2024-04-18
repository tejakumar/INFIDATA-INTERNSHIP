#object=real world entity
#to to solve real world problem
#class fan:boolean,on,off,string,brand,type,int,speed,plates,
#def rotation:

#def no rotation():

#variable:state
#function/method:behaviour
#concept:oops
# object,class,inherifance,polymorphism,encapsulation/abstraction,data entity
class addition:
    a,b,res=0,0,0

    def add(self):
        a=int(input("enter an int num1"))
        b=int(input("enter an int num2"))
        res=a+b
        print("add of {0} and{1} is{2}".format(a,b,res))

print("addition program using object orientation")
aobj=addition()
aobj.add()
print("a value:",aobj.a)
print("b value:",aobj.res)







