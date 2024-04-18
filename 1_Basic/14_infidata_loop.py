n1=int(input("enter n1"))
n2=int(input("enter n2"))
while(True):
        choice=int(input("enter ur choice:1 Add,2 Sub,3 Mult,4 Div, 5 Rem,6 Exit"))
        if (choice==1):
                  result=n1+n2
                  print("Add of {0} & {1} is {2}".format(n1,n2,result))
        elif (choice==2):
                  result=n1-n2
                  print("Sub of {0} & {1} is {2}".format(n1,n2,result))

        elif (choice==3):
                 result = n1*n2
                 print("Mult of {0} & {1} is {2}".format(n1, n2, result))
        elif (choice==4):
                 result = n1/n2
                 print("Div of {0} & {1} is {2}".format(n1, n2, result))
        elif (choice == 5):
                 result = n1%n2
                 print("Rem of {0} & {1} is {2}".format(n1, n2, result))


        else:
             exit(0)

