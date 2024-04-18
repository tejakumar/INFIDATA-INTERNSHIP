class Bank:
    def __init__(self):
        print('please create your account')
        self.name=input('enter your name:')
        self.id=int(input('enter your id:'))
        self.branch=input('enter your branch:')
        self.balance=int(input('enter your balance'))
    def deposit(self):
        self.dep=int(input('enter the amount to dep:'))
        self.balance+=self.dep
        print('amount deposited successfully and available balance is:', self.balance)
    def withdraw(self):
        self.wd = int(input('enter the amount to withdraw:'))
        if self.wd <=self.balance:
            self.balance -= self.wd
            print('amount withdrawn successfully and updated balance is:', self.balance)
        else:
            print('insufficient balance')
    def display(self):
        print('customer name:',self. name)
        print('customer id:', self.id)
        print('customer branch:', self.branch)
        print('Customer Available Balance;',self. balance)
print("Welcome to Online banaking")
bobj=Bank()

print("create ur account to proceed")

while True:
        print('1.deposit')
        print('2.withdraw')
        print('3.check balance')
        print('4.Exit')
        choice=int(input('enter your choice:'))
        if choice==1:

            bobj.deposit()
        elif choice==2:

            bobj.withdraw()
        elif choice==3:
            bobj.display()
        elif choice==4:
            exit(0)
        else:
            print('invalid choice')





