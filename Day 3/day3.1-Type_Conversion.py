#Type Conversion

#Interger to another type
print("= = = INTEGER TO ANOTHER TYPE = = =")
integer = 10

print("Integer to float : ", float(integer))
print("Interger to string : ", str(integer))
print("Interger to boolean : ", bool(integer))
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

#Float to another type
print("= = = FLOAT TO ANOTHER TYPE = = =")
dec_val = 10.25

print("Float to integer : ", int(dec_val))
print("Float to string : ", str(dec_val))
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

#String to another type
print("= = = STRING TO ANOTHER TYPE = = =")
string1 = "1025"  #"ABC" cannot be converted it will raise type error
string2 = "ABCAB"

print("String to integer :", int(string1))
print("String to float : ", float(string1))
print("String to list : ", list(string2))
print("String to tuple : ", tuple(string2))
print("String to set : ", set(string2))
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

#List to another types
print("= = = LIST TO ANOTHER TYPE = = =")
list1 = [1, 2, 3, 2, "prem", "sai"]

print("List to set : ", set(list1))
print("List to tuple : ", tuple(list1))
print("List to string : ", str(list1))
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

#Tuple to another types
print("= = = TUPLE TO ANOTHER TYPE = = =")
tuple1 = (1, 2, 3, 2, "prem", "sai")

print("Tuple to set : ", set(tuple1))
print("Tuple to list : ", list(tuple1))
print("Tuple to string : ", str(tuple1))
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

#Set to another types
print("= = = SET TO ANOTHER TYPE = = =")
set1 = {1, 2, 3, 2, "prem", "sai"}

print("Set to list : ", list(set1))
print("Set to tuple : ", tuple(set1))
print("Set to string : ", str(set1))
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")




