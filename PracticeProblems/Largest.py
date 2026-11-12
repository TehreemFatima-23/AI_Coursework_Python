number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if(number1 > number2):
    print("First input number is the largest")
elif(number2 > number1):
    print("Second input number is the largest")
else:
    print("Both the input numbers are equal")