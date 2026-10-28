
# ?	Find the sum of the first n natural numbers.

n = int(input("Enter a number: "))
total_sum = 0
# using loop first
for i in range(1, n + 1):
    total_sum = total_sum + i
print(f"The sum of first {n} natural numbers using loop is: {total_sum}")

# with the mathematical formula, we can also calculate the sum of first n natural numbers without using a loop.
total_sum = (n * (n + 1)) // 2
print(f"The sum of first {n} natural numbers is: {total_sum}")
