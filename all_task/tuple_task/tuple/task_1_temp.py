 temperature = int(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Freezing weather")
elif temperature <=10:
    print("Very Cold weather")
elif temperature <=20:
    print("Cold weather")
elif temperature <=30:
    print("Normal in Temp")
elif temperature >=40:
    print("It's Hot")
else:
    print("It's Very Hot")
