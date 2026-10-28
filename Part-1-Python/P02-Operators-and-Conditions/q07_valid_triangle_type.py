
# ? Check whether three sides form a valid triangle; if yes, print its type.

s1 = int(input("Enter 1st side of triangle : "))
s2 = int(input("Enter 2nd side of triangle : "))
s3 = int(input("Enter 3rd side of triangle : "))

if s1  + s2 > s3 and s1 + s3 > s2 and s2 + s3 >s1:
    print("It is Valid triangle")

    if s1 == s2 == s3:
        print("This is equilateral triangle")
    elif (s1 == s2) or (s1 == s3 ) or (s3 == s2 ):
        print("This is Isosceles triangle")
    else:
        print("This is Scalene triangle")
