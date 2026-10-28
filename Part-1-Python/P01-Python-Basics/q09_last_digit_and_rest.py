
# ? 09 - Take a 3-digit number and print its last digit and the number without the last digit.

three_digit = int(input("Enter any 3-Digit number : "))
last_digit = three_digit % 10
print(last_digit)

pending = three_digit // 10
print(pending)
