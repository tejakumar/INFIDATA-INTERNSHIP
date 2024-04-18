def check_number_present(num1,num2):
    if num2 in num1:
        print('the number is present in the list')
    else:
        print('the number is not present in the list')
l1=[1,2,3,4,5,6,7,8]
number=4
check_number_present(l1,number)