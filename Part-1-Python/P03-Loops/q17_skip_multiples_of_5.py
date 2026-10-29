
# ?	Print 1 to 20, skipping the multiples of 5 (continue).

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
