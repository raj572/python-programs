num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operation = input("Enter operation")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("invalid operation")