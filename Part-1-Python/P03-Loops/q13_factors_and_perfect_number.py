
# ?	Print all factors of a number and check whether it is a perfect number.

num = 24
factors = 0
for i in range (1, num + 1):
    if num % i == 0:
        factors = i
        print(factors)
        