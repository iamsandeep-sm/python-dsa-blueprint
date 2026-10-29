
# ?	Calculate the factorial of a number.

number = int(input("Enter a number: "))
fact = 1
for i in range(1, number + 1):
    fact = fact * i # this will multiply the current value of factorial with i
print("The factorial of", number, "is", fact)

# ! -------------------------------------------------------------------
#* another way to calculate factorial using while loop
if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    fact = 1
    i = 1
    while i <= number:
        fact = fact * i
        i = i + 1
    print(f"The factorial of {number} is {fact}")
