#WAP tp check which number is greater
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 > num2:
    print(f"The number {num1} is greater than {num2}")
elif num1 < num2:
    print(f"The number {num2} is greater than {num1}")
else:
    print("Both numbers are equal")