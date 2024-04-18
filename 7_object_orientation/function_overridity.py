class A:
    def display(self):
        print("am in class A")
class B(A):
    def display(self):
        print("am in class B")
bobj=B()
bobj.display()