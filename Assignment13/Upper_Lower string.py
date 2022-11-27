print("-----------------Upper Function Using Logic----------------------")
a = "hello, this is tejal jadhav from aitrc college "
print()
for i in a:
    x = ord(i)
    if(i == " "):
        print(" ", end = " ")
    elif(x >= 97 and x <= 122):
        c = x - 32
        
        print(chr(c), end = "")

print()
print()

print("-----------------Lower Function Using Logic----------------------")
d = "I LOVE VITA"
print()
for j in d:
    y = ord(j)
    if(j == " "):
        print(" ", end = " ")
    elif(y >= 65 and y <= 90):
        e = y + 32
        
        print(chr(e), end = "")

print()
print()
