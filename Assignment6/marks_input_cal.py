marks = []
i = 0

while(i < 5):
    a = int(input("Enter Your Marks : "))
    marks.append(a)
    i = i + 1
print("The list of marks are : " , marks , "\n")

i = 0
sum = 0

while(i < len(marks)):
    sum = sum + marks[i]
    i = i+1
print("Sumation of the Marks is : " , sum , "\n")

per = sum / 5
print("Percentage of the Marks is : " , per , "\n")

if(per < 100 and per > 75):
    print("Distinction")
elif(per < 75 and per > 60):
    print("First Class")
elif(per < 60 and per > 45):
    print("Second Class")
elif(per < 45 and per > 35):
    print("Pass")
elif(per < 35 and per > 0):
    print("Fail")
else:
    print("Thank you")
