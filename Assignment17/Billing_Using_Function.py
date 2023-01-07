def Billing(*a):
        amount = 0
        for i in a:
            amount = amount + i

        if(amount >= 1000 and amount <= 5000):
            
            print("your total bill is : " , amount)
            print()
            print("You got 2 percent discount")
            print()
            dis = amount * 0.02
            print("your discount is : " , dis)
            print()

            total = amount - dis
            print("You pay the total bill is : " , total)

        elif(amount >= 5000 and amount <= 10000):

            print("your total bill is : " , amount)
            print()
            print("You got 3 percent discount")
            print()
            dis = amount * 0.03
            print("your discount is : " , dis)
            print()
            total = amount - dis
            print("You pay the total bill is : " , total)

        elif(amount >= 10000 and amount <= 15000):

            print("your total bill is : " , amount)
            print()
            print("You got 5 percent discount")
            print()
            dis = amount * 0.05
            print("your discount is : " , dis)
            print()
            total = amount - dis
            print("You pay the total bill is : " , total)

        else:
            print("Sorry you got no discount")

Billing(120,2200,20,2400,2500)

