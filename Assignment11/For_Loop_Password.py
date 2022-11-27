password = input(" Enter password : ")
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0

for i in range(len(password)):
    
    if((len(password) >= 8)):
        flag1 = 1

        if(ord(password[i]) >= 65 and ord(password[i]) <=90):
            flag2 = 1

        elif(ord(password[i]) >= 97 and ord(password[i])<=122):
            flag3 = 1

        elif(ord(password[i]) >= 48 and ord(password[i])<=57):
            flag4 = 1

        elif((ord(password[i]) >= 58 and ord(password[i])<=64) or (ord(password[i]) >= 91 and ord(password[i])<=96) or ord(password[i]) >= 32 and ord(password[i])<= 47):
            flag5 = 1
        
if(flag2==1 and flag3==1 and flag4==1 and flag5==1):
    print("Valid Password")
    
else:
    print("Invalid password")
    print("Please Enter Eight Letters Strong Password")
    
