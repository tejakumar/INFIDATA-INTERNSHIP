T1 = (10, 20, 30, 40, 50, 60)
number = int(input("Enter a number to remove from the tuple: "))
T1_list = list(T1)
if number in T1_list:

    T1_list.remove(number)

    T1 = tuple(T1_list)

    print("Number removed successfully!")
    print("Updated tuple:", T1)
else:
    print("Number not found tuple.")

