#write a python program to calculate bill 
sum = 0
while(True):
    userInput = (input("Enter the price : "))
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"order total so far {sum}")
    else:
        print(f"Your total bill is {sum}. Thanks for shopping with us.")
        break
