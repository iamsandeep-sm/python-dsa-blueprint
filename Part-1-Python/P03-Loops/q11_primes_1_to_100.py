
# ?	Print all prime numbers between 1 and 100.

for num in range(1, 101):

    is_prime = True # assume number is prime until proven otherwise

    for i in range(2, num):
        if (num % i) == 0: # checking if number is divisible
            is_prime = False

    if is_prime == True:
        print(num)
