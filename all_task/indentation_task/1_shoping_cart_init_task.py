class Atransport:
    def __init__(self):
        self.name="_"
        self.w=0
        self.charge=0.0
    def accept(self):
        self.name=input("enter the name of the customer:")
        self.w=int(input("enter the weight of the parcel(in kg):"))
    def calculate(self):
        if self.w<=10:
            self.charge=self.w*25
        elif self.w<=20:
            self.charge=10*25+(self.w-10)*20
        else:
            self.charge=10*25+20*20+(self.w-30)*10
            self.charge=1.05        #add 5% subcharge
    def print(self):
        print("name:",self.name)
        print("weight:",self.w)
        print("bill amount:",self.charge)
transport=Atransport()       #create object of the class
transport.accept()            #invoke membership method
transport.calculate()
transport.print()