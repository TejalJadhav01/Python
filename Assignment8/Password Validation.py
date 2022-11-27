password = input("Enter Password : ")

i = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0

while(i < len(password)):
    
    if(len(password) >= 8):
        
        if(ord(password[i]) >= 65 and ord(password[i]) <= 90):
            flag1 = 1
            
        elif(ord(password[i]) >= 97 and ord(password[i]) <= 122):
            flag2 = 1
            
        elif(ord(password[i]) >= 48 and ord(password[i]) <= 57):
            flag3 = 1
            
        elif(ord(password[i]) >= 58 and ord(password[i]) <= 64):
            flag4 = 1
            
    else:
        print("password is less than 8 letters")
        break
    
    i = i + 1

if(flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1):
    print("password is valid")
    
else:
    print("invalid password")
    
    
