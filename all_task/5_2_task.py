def find_smallest_number(numbers):
    smallest=numbers[0]
    for num in numbers:
        if num<smallest:
            smallest=num
    return smallest
l1=[5,2,8,1,9]
smallest_number=find_smallest_number(l1)
print('the smallest number in the list l1 is:',smallest_number)