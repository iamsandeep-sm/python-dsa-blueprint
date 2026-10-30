
# ?	Print the first n terms of the Fibonacci series.

n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=' ') # used end=' ' to print the output within the same line
    a, b = b, a + b
    
#! FOR ANY BEGINNER THIS CODE MIGHT BE DIFFICULT TO UNDERSTAND LET ME EXPLAIN THIS
'''
n Python, the equal sign (=) splits the line into exactly two halves: a Left Side and a Right Side.
text
           LEFT SIDE             RIGHT SIDE
        (The variable boxes)      (The values)
          [ a , b ]        =     [ b , a + b ]

# blueprint to remember -
      
              VARIABLES             NEW VALUES
        [ a , b ]     =      [ b , a + b ]
          │   │                │     │
          └───┼────────────────┘     │
              └──────────────────────┘
'''
# ! - - - -- - - - - -- - - - - -- - -- - - - - - - - -- - -- -- - -- - -- - 
## * beginner level logic for solving this problem
    # temp = a
    # a = b
    # b = temp + b

## * another way to solve this problem
    # a = a + b
    # b = a- b
    