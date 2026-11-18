start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("\nEven Numbers")
for i in range(start, end + 1):
    if(i % 2 == 0):
        print(i)

print("\nOdd Numbers")
for i in range(start, end + 1):
    if(i % 2 != 0):
        print(i)
