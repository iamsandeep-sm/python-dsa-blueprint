
# ?	Print the multiplication table of a given number.
# taking input from user
num = int(input("Enter any number for table: "))
i = 1
while i <= 10:
    table = num * i 
    print(f"{num} X { i } : {table}")
    i = i + 1
    