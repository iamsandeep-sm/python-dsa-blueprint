
# ?	Check whether a number is an Armstrong number.
# armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

number = int(input("Enter a number: "))
temp = number
sum = 0
while temp > 0:
    digit = temp % 10 # this give us the last digit of number
    sum = sum + digit ** len(str(number)) # this is the formula for armstrong number
    temp = temp // 10 # this will remove the last digit from the number
    
if sum == number: # this check the sum is equals to the sum or not
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
    