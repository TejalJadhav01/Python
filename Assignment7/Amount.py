i=0
Total = 0
while(i < 100):
    Prices = int(input("Enter your prices : "))
    Total = Total + Prices
    b = input("You you want to continue (yes/no)")
    if(b == "no"):
      break
    
    i = i + 1
print("Your Total Amount is : " , Total)

if( Total > 5000 and Total < 7000):
    Dist = Total * 0.02
    print("You got 2% discount : " , Dist)
    Result = Total - Dist
    print("You pay the amount is :" , Result)

elif( Total > 7000 and Total < 10000):
    Dist = Total * 0.03
    print("You got 3% discount : " , Dist)
    Result = Total - Dist
    print("You pay the amount is :" , Result)

elif( Total > 10000 and Total < 100000):
    Dist = Total * 0.05
    print("You got 5% discount : " , Dist)
    Result = Total - Dist
    print("You pay the amount is :" , Result)

else:
    print("SomeThing Went Wrong")
