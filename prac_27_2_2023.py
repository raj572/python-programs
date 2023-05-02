# import sys
# sys.setrecursionlimit(10**8)
# def rec_fact(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_fact(n-1)
# n=int(input('Enter number : '))
# if n==0:
#     print('Factorial of 0 is 1.')
# elif n<0:
#     print('sorry, factorial does not exist for negative numbers.')
# else:
#     print('Factorial of ',n,"is ", rec_fact(n))

def sum_arr(arr,size):
   if (size == 0):
     return 0
   else:
     return arr[size-1] + sum_arr(arr,size-1)
n=int(input("Enter the number of elements for list:"))
a=[]
for i in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)
print("The list is:")
print(a)
print("Sum of items in list:")
b=sum_arr(a,n)
print(b)