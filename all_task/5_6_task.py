def interchange_first_last(num):
    if len(num)>=2:
        num[0],num[-1]=num[-1],num[0]
    return num
l1=[9,8,7,6,5,4,3,2,1]
interchanged_list=interchange_first_last(l1)
print('list after interchanging first and last element is:',interchanged_list)