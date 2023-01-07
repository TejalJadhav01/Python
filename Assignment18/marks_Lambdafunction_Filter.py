marks = [45,67,89,23,14,45,56]

result = list(filter(lambda i : i>=75 , marks))
result1 = list(filter(lambda i : i>=60 , marks))
result2 = set(filter(lambda i : i>=55 , marks))
result3 = list(filter(lambda i : i>=35 , marks))
result4 = tuple(filter(lambda i : i<35 , marks))

print(" The student pass with Distinction : " , result)
print(" The student pass with First Class : " , result1)
print(" The student pass with Second Class : " , result2)
print(" The student pass : " , result3)
print(" The Fail Students fail : " , result4)

