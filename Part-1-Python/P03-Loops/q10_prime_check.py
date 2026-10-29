
# ?	Check whether a number is prime.

number = int(input("Enter a number: "))
i = 1
if number > 1:
    for i in range (2 , number):
        if (number % i) == 0:
            print("", number, "is not a prime number")
            break
    else:
        print(f"{number} is prime number")
