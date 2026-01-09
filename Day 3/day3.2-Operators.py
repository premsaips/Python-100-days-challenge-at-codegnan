#Operators

# Arithmetic operators
print("= = = ARTHEMETIC OPERATORS = = =")

num1 = 10
num2 = 5

print("Addition:", num1 + num2)                # Addition
print("Subtraction:", num1 - num2)              # Subtraction
print("Multiplication:", num1 * num2)         # Multiplication
print("Division:", num1 / num2)                 # Division 
print("Modulo Division:", num2 % num1)   # Modulo Division
print("Floor Division :", num1 // num2)      # Floor Division
print("Exponentiation:", num1 ** num2)     # Exponentiation
print("----------------------------------------------------------------------------")

#Relational / Comparision Operators
print("= = = RELATIONAL / COMPARISION OPERATORS = = =")
num1 = 10
num2 = 5

print("Equal to:", num1 == num2)        # Equal to
print("Not equal to:", num1 != num2)    # Not equal to
print("Greater than:", num1 > num2)     # Greater than
print("Less than:", num1 < num2)        # Less than
print("Greater than or equal to:", num1 >= num2)    # Greater than or equal to
print("Less than or equal to:", num1 <= num2)       # Less than or equal to
print("----------------------------------------------------------------------------")

# Logical operators
print("= = = LOGICAL OPERATORS = = =")
value1 = 5
value2 = 7

print("Logical AND:", value1>10 and value2<10)      # Logical AND
print("Logical OR:", value1>10 or value2<10)         # Logical OR
print("Logical NOT:", not value1>10)                     # Logical NOT
print("----------------------------------------------------------------------------")

#Assignment Operators
print("= = = ASSIGNMENT OPERATORS = = =")
num1 = 10

num1 += 1 
print("Addition Equals to : ", num1)           #Addition Equals to
num1 -= 1
print("Subtraction Equals to : ", num1)         #Subtraction Equals to
num1 *= 2
print("Multiplication Equals to : ", num1)   #Multiplication Equals to
num1 /= 2
print("Division Equals to : ", num1)             #Division Equals to
num1 %= 4
print("Modulus equal to : ", num1)            #Modulus equal to
num1 **= 3
print("Exponential Equal to : ", num1)      #Exponential Equal to
num1 //= 3
print("Floor Division Equals to : ", num1)  #Floor Division Equals to
print("----------------------------------------------------------------------------")

#Bitwise Operations
print("= = = BITWISE OPERATORS = = =")
x=5
y=3

print (" AND (&) is:",(x&y))        # AND (&)
print (" OR (|) is:",(x|y))             # OR (|)
print (" XOR (^) is:",(x^y))          # XOR (^)
print (" Not (~) is:",(~x))            # Not (~)
print (" Shift Right(>>) is:",(x>>1))   # Shift Right(>>)
print (" Shift Left (<<) is:",(x<<2))    # Shift Left (<<)
print("----------------------------------------------------------------------------")

# Membership operators
print("= = = MEMBERSHIP OPERATORS = = =")
fruits = ["apple", "banana","prem", "cherry"]

print("Membership (in):", "ramya" in fruits)    # Membership - in
print("Membership (not in):", "prem" not in fruits)     # Membership - not in
print("----------------------------------------------------------------------------")

# Identity operators
print("= = = IDENTITY OPERATORS = = =")
x = "prem"
y = 5

print("Identity (is):", x is y)   # Identity - is
print("Identity (is not):", x is not y)     # Identity - is not
print("----------------------------------------------------------------------------")












