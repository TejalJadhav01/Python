marks = [23,45,67,[78,98,59,89],56,77,56.89,89,(23,45,56,78,90,99),56.90,45.67]

sum = 0
for i in range(len(marks)):
    

    List_type = type(marks[i])
    
    if(List_type == int or List_type == float):
        sum = sum + marks[i]
        
    elif(List_type == list or List_type == tuple):
        for j in range(len(marks[i])):
            
            sum = sum + marks[i][j]
            
print("Sum of all elements in the list : " , sum)
    
