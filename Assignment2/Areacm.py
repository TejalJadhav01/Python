#Area Of Circle

print("Area Of Circle \n")
radius = input("Enter Radius:")
z = int(radius)
print("radius :", z,"cm","\n")
x = 3.14 * z * z
print("Area of circle in CM : ",x,"CM")

area_of_circle_in_MM = x * 10
print("area_of_circle_in_MM :" ,area_of_circle_in_MM,"MM")

area_of_circle_in_M = x / 100
print("area_of_circle_in_M :" ,area_of_circle_in_M,"M")

area_of_circle_in_ft = x / 30.48
print("area_of_circle_in_ft :" ,area_of_circle_in_ft,"ft" ,"\n\n")


#Area Of Reactangle

print("Area Of Rectangle \n")
length = input("Enter the Length of rectangle : ")
width = input("Enter the Width of rectangle : ")
x = int(length)
y = int(width)
print("\n")

print("Length of Rectangle :", x,"cm")
print("Width of Rectangle :", y,"cm" ,"\n")


z = x * y
print("Area of Rectangle in CM : ",z,"CM")

area_of_Rectangle_in_MM = z * 10
print("area_of_Rectangle_in_MM :" ,area_of_Rectangle_in_MM,"MM")

area_of_Rectangle_in_M = z / 100
print("area_of_Rectangle_in_M :" ,area_of_Rectangle_in_M,"M")

area_of_Rectangle_in_ft = z / 30.48
print("area_of_Rectangle_in_ft :" ,area_of_Rectangle_in_ft,"ft","\n\n")

#Area of Square

print("Area Of Square \n")

side = input("Enter the value:")
x = int(side)
print("side : ",x,"CM","\n")
z = x * x
print("Area of Square in CM : ",z,"CM")

Area_of_Square_in_MM = z*10
print("Area of Square in MM :" ,Area_of_Square_in_MM,"MM")

Area_of_Square_in_M = z / 100
print("Area of Square in M :" ,Area_of_Square_in_M,"M")

Area_of_Square_in_ft = z / 30.48
print("Area of Square in ft :" ,Area_of_Square_in_ft,"ft")



