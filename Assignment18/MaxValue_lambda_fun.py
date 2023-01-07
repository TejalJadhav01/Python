a = lambda x,y,z : x if(x>y and x>z) else y if(y>x and y>z) else z

print("max value is : " , a(23,56,45))
print("max value is : " , a(23,56,415))

