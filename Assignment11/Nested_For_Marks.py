marks = [[90,80,89,76,89],[89,78,90,94,76],[67,89,87,78,90],[97,78,94,92,65]]

Total_marks = []
Per_marks = []

for i in marks:

    sum = 0
    per = 0
    
    for j in i:
        
        sum = sum + j
        
    for k in i:

        per = sum / 5
        
    Per_marks.append(per)

    Total_marks.append(sum)

    
print("Total Marks of each student is : " , Total_marks)
print("percentage is of each student is : " , Per_marks)


