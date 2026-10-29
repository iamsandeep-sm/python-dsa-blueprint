
# ?	Reverse a number (1234 -> 4321) and check whether it is a palindrome.

num = 1234
#temp = abs(number) ## used only when asking user to give input this will handle the negative numbers

original_num = num 
reversed_num = 0

while num > 0:
    digit = num % 10 # it gives us the last digit
    reversed_num = (reversed_num * 10) + digit  # store the digit and make space for other number
    num = num // 10  # this remove the last digit

print(f"Reversed number: {reversed_num}")

if original_num == reversed_num:
    print(f"{original_num} is a palindrome number.")
else:
    print(f"{original_num} is NOT a palindrome number.")
    