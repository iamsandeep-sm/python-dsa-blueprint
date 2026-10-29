
# ?	Print 1 to 100, but stop at the first number divisible by 17 (break).

for i in range(1, 101):
    if i % 17 == 0:
        break
    print(i)
