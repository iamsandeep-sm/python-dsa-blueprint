
# ? Calculate simple interest for a given principal, rate and time.

p = float(input("Enter principal amount : "))
r = float(input("Enter rate : "))
t = float(input("Enter the time period : "))

SI = (p * r * t) / 100
total_si = p + SI
print(f"The simple interest is {total_si}")

total_ci= p * (1 + r /100) ** r
CI = total_ci -p
print(f"The compound interest is {CI:.2f}")
