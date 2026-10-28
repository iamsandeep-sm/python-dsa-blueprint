
# ? Check whether a number is divisible by both 3 and 5.

num = int(input("Enter any number : "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif num % 3 == 0:
    print("The number is divisible by 3")
elif num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is neither divisible by 3 nor 5")     
    