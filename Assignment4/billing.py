amount = float(input("Enter Your Amount :"))

if(amount >= 1000 and amount < 1500):
    dis = amount * 0.02
    result = amount - dis
    print("Discount of 2 percent : " , dis)
    print("You pay the remaining amount is : " ,result)
    
elif(amount >= 1500 and amount < 2000):
    dis = amount * 0.03
    result = amount - dis
    print("Discount of 3 percent : " , dis)
    print("You pay the remaining amount is : " ,result)
    
elif(amount >= 2000 and amount < 100000000000):
    dis = amount * 0.05
    result = amount - dis
    print("Discount of 5 percent : " , dis)
    print("You pay the remaining amount is : " ,result)
    
else:
    print("Thank u for visiting us")
