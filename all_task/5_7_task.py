def count_even_odd(numbers):
    even_count=0
    odd_count=0
    for num in numbers:
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    print('number of even numbers:',even_count)
    print('number of odd numbers:',odd_count)
l1=[1,2,3,4,5,6,7,8,9,10,12]
count_even_odd(l1)