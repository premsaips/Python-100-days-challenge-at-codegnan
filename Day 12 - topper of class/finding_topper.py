#who is topper
print("welcome to the topper")
n = int(input("enter number of the student in the class:"))
names = []
marks = []
class_marks=[]
percentage=[]

print("Enter the all student marks")
for i in range(n):
    print(f"Enter the roll number{i+1}student marks")
    name = input("Enter the student name:")
    print("Enter the Telugu,English,Hindi,Maths,Science,Social marks,as per the oder")
    Telugu, English, Hindi, Maths, Science, Social=map(int,input().split()[:6])
    total_marks = Telugu + English + Hindi + Maths + Science + Social
    std_percentage = (total_marks/600)*100
# store all values in list
    names.append(name)
    marks.append([Telugu, English, Hindi, Maths, Science, Social])
    class_marks.append(total_marks)
    percentage.append(std_percentage)
#print the topper details
print("Topper in the class is")
top_marks = max(class_marks) 
topper_pos = []
for i in range(n):
    if class_marks[i] == top_marks:
        topper_pos.append(i)
#print the topper details
for i in range(len(topper_pos)):
    print("Name of the student is:", name[i])
    print("Marks of the student is:", marks[i])
#Each student marks
for i in range(n):
    print("Name of the student is:", names[i], "Marks is:", marks[i])