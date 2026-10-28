
# ? Find the largest of three numbers using if-elif-else.

num1 = int(input("Enter you first number : "))
num2 = int(input("Enter you second number : "))
num3 = int(input("Enter you third number : "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest number among both the number you entered")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest number among both the number you entered")
else:
    print(f"{num3} is the largest number among both the number you entered")
