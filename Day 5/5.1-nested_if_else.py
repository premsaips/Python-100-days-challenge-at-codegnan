#Check weather the given number is positive even/ positive odd/ negitive even/ negitive odd.

n = int(input())

if n % 2 == 0:
    if n > -1:
        print("Positive even.")
    else:
        print("Positive odd.")
else:
    if n > -1:
        print("Negitive even")
    else:
        print("Negitive Odd")
