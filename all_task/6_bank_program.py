def customer_details():
    global name,id,branch,balance
    name=input('enter customer name: ')
    id=int(input('enter customer id:'))
    branch=input('enter customer branch:')
    balance=int(input('enter an amount to create account:'))

def deposit(amount):
    global balance
    balance+=amount
    print('amount deposited successfully and available balance is:',balance)
def withdraw(amount):
    global balance
    if amount<=balance:
        balance-=amount
        print('amount withdrawn successfully and updated balance is:',balance)
    else:
        print('insufficient balance')
def display():
    print('customer name:',name)
    print('customer id:',id)
    print('customer branch:',branch)
    print('Customer Available Balance;',balance)

print("Welcome to Online banaking")
print("create ur account to proceed")
customer_details()

while True:
        print('1.deposit')
        print('2.withdraw')
        print('3.check balance')
        print('4.Exit')
        choice=int(input('enter your choice:'))
        if choice==1:
            amount=int(input('enter the amount of deposite :'))
            deposit(amount)
        elif choice==2:
            amount=int(input('enter the amount to withdraw:'))
            withdraw(amount)
        elif choice==3:
            display()
        elif choice==4:
            exit(0)
        else:
            print('invalid choice')

