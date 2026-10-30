
# ?	Find the HCF and LCM of two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b  #*  Shifting the values just like in Fibonacci problem i did
    
hcf = a
lcm = (num1 * num2) // hcf  #*  LCM formula : LCM = (num1 * num2) / HCF

print(f"The HCF of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")

