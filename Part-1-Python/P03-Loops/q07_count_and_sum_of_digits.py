
# ?	Count the digits of a number and find the sum of its digits.
##* beginner friendly code and the logic to understand how this kind of question is being solved
'''
number = int(input("Enter a number: "))
unit = number % 10
ten = (number // 10) % 10
hundred = (number // 100)
sum_of_digits = unit + ten + hundred
'''

##! -----------------------------------------------------------------------
##* now the actual code using the loop for this question....
number = int(input("Enter a number: "))
temp = abs(number)  # it handle negative numbers

digit_count = 0
sum_of_digits = 0

if temp == 0:
    digit_count = 1
    sum_of_digits = 0
else:
    while temp > 0:
        unit = temp % 10            # out the last digit
        sum_of_digits += unit       # adding last digit to the total sum
        digit_count += 1            # Increment the count of digits
        temp = temp // 10           # Remove the last digit from the number so that we can store the another number in the next iteration

print("Total number of digits:", digit_count)
print("The sum of the digits is:", sum_of_digits)

