numbers = int(input("Enter the marks: "))

while numbers < 0 or numbers > 100:
    print("Invalid marks. Enter again...")
    numbers = int(input("Enter the marks again: "))

if numbers >=90:
    print("A+")
elif numbers >=80:
    print("A")
elif numbers >=70:
    print("B")
elif numbers >=60:
    print("C")
elif numbers >=50:
    print("D")
else:
    print("Fail")