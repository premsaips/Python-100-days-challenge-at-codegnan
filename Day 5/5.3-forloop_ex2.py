#Check weather the number is even positive or odd positive or even negitive or odd negitive in a list of numbers

lst = [1,-2,-4,-6,-5,3,45,7,8]

for num in lst:
    if num > -1:
        if num % 2 == 0:
            print(num, " is positive even")
        else:
            print(num, " is positive odd")
    else:
        if num % 2 == 0:
            print(num, " is negitive even")
        else:
            print(num, " is negitive odd")

