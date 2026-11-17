number1 = int(input("Enter the First number: "))
number2 = int(input("Enter the Second number: "))

op = input("Enter the operator(+, -, *, /): ")

if (op == '+') :
    print("Addition: ", number1 + number2)
elif (op == '-') :
    print("Subtraction: ", number1 - number2)
elif (op == '*') :
    print("Multiplication: ", number1 * number2)
elif (op == '/') :
    if (number2 == 0) :
        print("Cannot Divide by 0")
    else:    
        print("Division: ", number1 / number2)
else:
    print("Invalid operator")