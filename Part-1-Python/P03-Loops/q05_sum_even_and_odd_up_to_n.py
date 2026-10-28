
# ?	Find the sum of all even numbers and of all odd numbers up to n.
#* beginner friendly program to find the sum of even and odd numbers up to n.
n = int(input("Enter a number: "))
sum_even = 0
i = 1
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even = sum_even + i
print(f"The sum of even numbers up to {n} is: {sum_even}")

sum_odd = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum_odd = sum_odd + i
print(f"The sum of odd numbers up to {n} is: {sum_odd}")


#* Better way to code the same problem is to use a single loop to find the sum of even and odd numbers up to n.
#! we can use a single for loop or a single while loop to find the sum of even and odd numbers up to n.
'''
n = int(input("Enter a number: "))
sum_even = 0
sum_odd = 0
i = 1

# working within single for loop
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
# * ------------------------------------------------------------------------
# here i worked with using single while loop
while i <= n:
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
    i = i + 1

print(f"The sum of even numbers up to {n} is: {sum_even}")
print(f"The sum of odd numbers up to {n} is: {sum_odd}")

'''
