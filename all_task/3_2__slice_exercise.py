def mystery (num_list):
    sum=0
    for i in range(0,len(num_list),2):
        num=num_list[i]
        sum+=num
        return sum
list1=[1,2,3,4]
print(mystery(list1))