lst = [45,56,67,89,67,23,12,89,79]

even = list(filter(lambda i : i % 2 == 0 , lst))
odd = set(filter(lambda i : i% 2 != 0 , lst))


print("Even No list : " , even)
print("Odd No : " , odd)

