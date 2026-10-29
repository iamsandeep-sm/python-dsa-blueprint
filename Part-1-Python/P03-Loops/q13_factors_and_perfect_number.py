
# ?	Print all factors of a number and check whether it is a perfect number.
'''
num = int(input("Enter any number to check its factor and perfect number or not? : "))
factors = 0
for i in range (1, num + 1):
    if num % i == 0:
        factors = i
        print(factors)
#* the another part of the problem is below down -- is it perfect number or not.....
factors_sum = 0
for i in range(1, num):
    if num % i == 0:
        factors_sum += i

if factors_sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
'''
#! --------------------------------------------------------------------------

#* within single loop the better code for the same problem-

num = int(input("Enter any number to check its factor and perfect number or not? : "))
factors_sum = 0
print(f"The factors of {num} are -")
for i in range (1, num + 1):
    if num % i == 0:
        print(i)
    if i < num: # it checks number exclude the number it-self
        factors_sum += i
        
if factors_sum == num:
    print(f"The number {num} you entered is perfect number")
else:
    print(f"The number {num} is not a perfect number")
