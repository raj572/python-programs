num = int(input("Enter the number to check it is prime or not : "))
prime = True
for i in range(2,num):
    if (num%2==0):
        prime = False
        break
if prime:
    print("This is prime number")
else:    
    print("This is not prime number")        
    