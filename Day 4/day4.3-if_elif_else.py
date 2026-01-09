#IF ELIF ELSE STATEMENT

#Ex-1. Check wheather the number is 1.+ve even, 2.-ve even, 3. +ve odd, 4.-ve odd

num = int(input())

if (num % 2 ==0 and num >= 0):
    print(" Number is even positive")
elif (num % 2 != 0 and num >= 0):
    print("Number is odd positive.")
elif(num % 2 == 0 and num < 0):
    print("Number is even negitive.")
elif(num % 2 != 0 and num < 0):
    print("Number is Odd negitive.")
else:
    print("Enter valid number")
