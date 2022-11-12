a = [[1,2,3,4,5],[6,7,8,9,10],[2,4,6,8,10]]
i=0
sum=0
marks=[]
while(i < len(a)):
    j = 0
    while(j < len(a[i])):
        sum = sum + a[i][j]
        j = j + 1
    marks.append(sum)
    i = i + 1
print(marks)

