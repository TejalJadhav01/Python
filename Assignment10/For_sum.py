# Program for to  print the sum of the numbers

sum = 0
a=[1,2,3,4,5]
for i in a:
    sum = sum + i
print("Sum is : " , sum)


# Program for To print the Total and Percentage of given marks with grade.

marks = [90,96,88,87,93]
sum = 0
for i in marks:
    sum = sum + i
    
print("Total Marks is : " , sum)

per = sum/5
print("percentage is : " , per)

if(per >= 75 and per < 100):
    print("Distinction")

elif(per >= 60 and per < 75):
    print("First Class")
    
elif(per >= 45 and per < 60):
    print("Second Class")
    
elif(per >= 35 and per < 45):
    print("Pass")

elif(per >= 0 and per < 35):
    print("oops..! You are Fail")
    
else:
    print("Thank you")


