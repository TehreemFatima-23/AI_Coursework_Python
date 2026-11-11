enteredValue = int(input("Enter the number till you want to calculate the sum: "))
sum = 0
# for loop to iterate the numbers
for i in range(1, enteredValue + 1):
    sum += i

print ("Sum of the numbers till the entered number is: ", sum)    