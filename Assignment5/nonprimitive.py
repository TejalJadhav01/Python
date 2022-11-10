a = [1,45,"Tejal",67,3.14,True,97,98,101 ,45,45]
print("Type : ", type(a), " List is : " ,a , "\n")

#slicing

print("print 45 element to 97 element : " , a[1:7] , "\n\n")

print("Print 1 element to True element : " ,a[ :6],"\n\n")

print("Print 'Tejal' element to 101 element : " , a[2:] , "\n\n")  

print("Reverse List is : " , a[9: :-1],"\n\n")

print(".Print to the 1 ,'Tejal',3.14,97,101 : ",a[0:9:2],"\n\n")

# List Attributes
a.append("BTECH")
print("Append Element list : " , a , "\n\n")

a.insert(5,"False")
print("Insert Element at 5 index of False Element : " , a)

a.extend("abcde")
print("Extend Elements:" , a ,"\n")

a.remove(101)
print("removed : " , a , "\n")

a.pop(6)
print("poped : " , a , "\n")

print("index value : ", a.index(67) , "\n")

print("count of 45 is : " , a.count(45), "\n")
a.clear()
print("cleared : ", a)
      
# Tuple Attributes

b = (1,3,4.56,True,"Tejal",78,4.56,88.98,4.56)
print(type(b) , b)

print("index is : " , b.index("Tejal"), "\n")

print("count is : " , b.count(4.56), "\n")


#Dictionary

c = {1:"abc",2:"xyz",3:"pqr",4:"uvw"}
print(type(c),c)

#Nested List

d = (1,3,4.56,(1,2,3,4,5),True,"Tejal",78,(5,4,3,2,1),88.98)
print(d)
print(d[3])
print(d[3][4])
print(d[7])
print(d[7][2])

#Set

e={11,23,"tejal",33.77}
print(type(e),e)


# Type Casting
# List
list1 = [1,3,67,89,"Tejal",True,3.14,96]
print(type(list1), "list is: ",list1)

z = tuple(list1)
print(type(z),z)

z = set(list1)
print(type(z),z)

# Tuple

Tuple = (1,3,67,89,"Tejal",True,3.14,96)
print(type(Tuple),Tuple)

y = list(Tuple)
print(type(y),y)

z = set(Tuple)
print(type(z),z)


# Set

set1 = {1,3,67,89,"Tejal",True,3.14,96}
print(type(set1),set1)

y = list(set1)
print(type(y),y)

z = tuple(set1)
print(type(z),z)


# Dictionary

m = [1,2,3,4,5,6]
n = ["Tejal","Kajal","Priyanka","Shiv","Sahil"]
h = zip(m,n)
g = dict(h)
print(g,h)

m = [1,2,3,4,5,6]
n = ["Tejal","Kajal","Priyanka","Shiv","Sahil"]

print(dict(zip(m,n)))
