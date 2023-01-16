print("-------For Loop-------")
class marks():
    
    def add(self,*m):
        sum = 0
        for i in m :
            sum = sum + i
        print(sum)


m = marks()
m.add(89,56,45,56,43)


print("-------While Loop-------")

class Marks():
    
    def add1(self,*m):
        s = 0
        i=0
        while(i<len(m)):
            s = s + m[i]
            i = i + 1
        return s

m1 = Marks()
Marks = m1.add1(89,56,45,56,43)
print(Marks)
