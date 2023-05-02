from posixpath import split


# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))
# average = (a+b+c)//3
# print("average of these numbers is 3" + str(average))
#or
num1,num2,num3 = input("Enter three numbers with comma ").split(",")
print(f"average of three numbers is : {(int(num1)+int(num2)+int(num3))/3}")
