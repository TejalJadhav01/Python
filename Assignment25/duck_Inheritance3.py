class circle():
    def area(self):
        print("area of circle")
        print("Radius of circle is 14")
        print("3.14*r*r")
        
class Rectangle():
    def area(self):
        print("Area of rectangle ")
        print(" The base of rectangle is 10cm")
        print(" The height of rectangle is 5cm")

class square():
    def shapes(self ,a1):
        a1.area()

s1 = square()
r = Rectangle()
c = circle()
s1.shapes(r)
s1.shapes(c)
        
        
