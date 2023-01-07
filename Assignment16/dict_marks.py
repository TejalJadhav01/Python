marks = {"Anushka":[62,72,22,82,87],"Afsana":[78,90,45,67,78],"kajal":[62,72,67,82,87],"Tejal":[78,90,50,67,78]}
lst1 = []
lst2 = []
flag = 0
for i in marks:
    s=0
    lst1.append(i)
    for j in marks[i]:
        if(j<35):
            flag=1
        s=s+j
    per=s/5
    lst2.append(per)
    if(flag==1):
        print(i,"has fail")
        flag=0
    elif(per>35 and per <50):
        print("has pass with",per)
    elif(per>=50 and per<60):
        print("second class with",per)
    elif(per>=60 and per<75):
        print(i,"dist with",per)
    print("------------------------------------")
d=dict(zip(lst1,lst2))
m=max(lst2)
for p in d:
    if(m==d[p]):
        print("topper is ",p,"with",d[p])
