
# ?	Keep taking numbers until 0 is entered, then print their sum.

num = int(input("Enter a number (0 to stop): "))
total_sum = 0
while num != 0:
    total_sum = total_sum + num
    num = int(input("Enter a number (0 to stop): "))
