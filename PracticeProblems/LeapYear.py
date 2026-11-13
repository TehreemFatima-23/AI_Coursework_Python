year = int(input("Enter the number you want to check: "))
#check if the entered year is leap year or not

if (year  % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")