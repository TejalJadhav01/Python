def marks():

    a = [[56,78,87,76,74],[76,45,56,76,87],[56,67,87,86,85]]
    
    list1 = []
        
    for i in a:
        sum = 0
        for j in i:
            sum = sum + j
        list1.append(sum)
    return list1
        

b = marks()
print("Sum is : " , b)

#print(marks())

list2 = []

for k in marks():

    per = k/5
    list2.append(per)

print("percentage list : " , list2)
