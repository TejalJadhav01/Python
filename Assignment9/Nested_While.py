# Find the sum of all elements to the list.


a = [45,78,90,[6779,568,89.90],436,89,(234,890,32,),67,89,[54,823,789],67,90]
sum = 0
i=0
while(i < len(a)):
    b = str(type(a[i]))
    
    if(b == "<class 'int'>" or b == "<class 'float'>"):
        sum = sum + a[i]
        
    elif(b == "<class 'list'>" or b == "<class 'tuple'>"):
        j = 0
        while(j < len(a[i])):
            sum = sum + a[i][j]
            
            j = j + 1
    i = i + 1
print(sum)
