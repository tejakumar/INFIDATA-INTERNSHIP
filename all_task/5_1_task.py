def find_largest_number(numbers):
    largest=numbers[0]
    for num in numbers:
        if num>largest:
            largest=num
    return largest
l1=[5,2,8,1,9]
largest_number=find_largest_number(l1)
print('the largest number in the list l1 is:',largest_number)