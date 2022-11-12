# Show the Even And Odd Numbers from 1 to 100

i=0

while(i<101):

    if(i%2==0):
        print("Even number is : " , i)

    else:
        print("Odd number is : " , i)

    i=i+1

print("thank you")


# Sum of Even and Odd Numbers from 1 to 20

i=1

Even_Sum = 0
Odd_Sum = 0

while(i < 21):
    
    if(i % 2 == 0):
        Even_Sum = Even_Sum + i

    else:
        Odd_Sum = Odd_Sum + i

    i=i+1

print("Sum of Even Numbers : " , Even_Sum)
print("Sum of Odd Numbers : " , Odd_Sum)

    
