a = input("Please Enter Here : ")

c = ""
s = ""
n = ""
sy = ""

for i in a:

    if(ord(i) >= 65 and ord(i) <= 90):
        c = c + i
        
    elif(ord(i) >= 97 and ord(i) <= 122):
        s = s + i
        
    elif(ord(i) >= 48 and ord(i) <= 57):
        n = n + i
        
    elif((ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i)<= 96) or (ord(i) >= 32 and ord(i) <= 47)):
        sy = sy + i
        
total = c+s+n+sy
print(total)
