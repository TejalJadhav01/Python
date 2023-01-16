class Marks():
    
    def add1(self,*m):
        total = []
        for i in m:
            sum=0
            for j in i:
                sum = sum + j

            total.append(sum)

        return total
    
        
            
m1 = Marks()
Marks = m1.add1((89,56,45,56,43),(89,56,45,56,43),(89,56,45,56,43))
print(Marks)
