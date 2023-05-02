number = int(input("Enter the number to get factorial : "))
factorial = 1
for i in range(1,number+1):
    factorial = factorial*i
print(f"The factorial of a number is {factorial}")    