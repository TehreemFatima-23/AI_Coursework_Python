number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 > number2 and number1 > number3:
    print("First input number is the largest")
elif number2 > number1 and number2 > number3:
    print("Second input number is the largest")
elif number3 > number1 and number3 > number2:
    print("Third input number is the largest")
elif number1==number2==number3:
    print("All the three input numbers are equal")
else:
    print("Two or more share the largest input")