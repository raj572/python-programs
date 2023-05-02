# character pattern
"""E
   DE
   CDE
   BCDE
   ABCDE"""

# n = int(input())
# row=1
# while row<=n:
#     col=0
#     while col<row:
#         k=65+n-row
#         print( chr(k+col),end='')
#         col=col+1
#     print()
#     row=row+1

# 55555
# 4444
# 333
# 22
# 1

# n=int(input())
# row=1
# while row<=n:
#     col=1
#     while col<=n-row+1:
#         print(n-row+1,end='')
#         col=col+1
#     print()
#     row=row+1


#     *
#    ***
#   *****
#  *******
# *********


# n=int(input())
# row=1
# while row<=n:
#     spaces=1
#     while spaces<=n-row:
#         print(' ',end='')
#         spaces=spaces+1
#     col=1
#     stars=1
#     while col<=row:
#         print('*',end='')
#         col=col+1
#         stars=stars+1
#     stars=row-1
#     while stars>=1:
#         print('*',end='')
#         stars=stars-1
#     print()
#     row=row+1

'''
    1
   232
  34543
 4567654
567898765
'''

# n=int(input())
# d=n//2+1
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         if(y>=d)!=0 and y<=n-d+1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     if x<=n//2:
#         d-=1
#     else:
#         d+=1
#     print()

'''''''''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

# n=int(input())
# #loop for rows
# row=1
# while row<=n:
#     #loop for spaces
#     space=1
#     while space<=n-row:
#         print(' ',end='')
#         space=space+1
#     #loop for stars
#     col = 1
#     while col<=row*2-1:
#         print('*',end='')
#         col+=1
#     print()
#     row+=1
# #2nd pattern
# #loop for rows
# row=n-1
# while row>=1:
#     #loops for spaces
#     space=1
#     while space<=n-row:
#         print(' ',end='')
#         space+=1
#     #loops for stars
#     col=1
#     while col<=2*row-1:
#         print('*',end='')
#         col+=1
#     print()
#     row=row-1

# *0000*0000*
# 0*000*000*0
# 00*00*00*00
# 000*0*0*000
# 0000***0000


# n = int(input())
# i = 1
# j=1
# while i<= n:
#     j = 1
#     while j <= n:
#         if i==j:
#             print('*',end = '')   
#         else:
#             print('0',end = '')
#             j = j + 1
#     j=j-1
#     print("*",end="")
#     while j>=1:
#         if i==j:
#             print('*',end = '')   
#         else:
#             print('0',end = '')
#     j = j - 1    
#     print()
#     i = i + 1

# 1234
#  234
#   34
#    4
#   34
#  234
# 1234

# n=int(input())
# row = 1
# while row<=n:
#     space=2
#     while space<=row:
#         print('-',end='')
#         space+=1
#     col=n-row
#     while col>=0:
#         print(n-col,end='')
#         col-=1
#     print()
#     row+=1
# row=2
# while row<=n:
#     space=1
#     while space<=n-row:
#         print('-',end='')
#         space+=1
#     col=1
#     while col<=row:
#         print(col,end='')
#         col+=1
#     print()
#     row+=1



# n = int(input())
# for i in range(1,n+1):
#     count=1
#     for j in range (1,i):
#         print(' ',end='')
#         count +=1
#     num = i
#     for j in range(count,n+1):
#         print(num,end='')
#         num +=1
#     print()
# for i in range(n-1,0,-1):
#     count =1
#     for j in range(1,i):
#         print(" ",end='')
#         count +=1
#     num =i
#     for j in range(count,n+1):
#         print(num,end="")
#         num +=1
#     print()

# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334  
# 4444444

# def square(a):
#     ans  = a*a
#     return  ans

# a = 4
# a = square(a)
# print(a)       
'''
5432*
543*2
54*21
5*321
*4321
'''
'''
A
AB
ABC
ABCD
'''
# n=int(input())
# row=1
# while row<=n:
#   col=1
#   while col<=row:
#     print(chr(64+col),end='')
#     col+=1
#   print()
#   row+=1
'''
12344321
123**321
12****21
1******1
'''
# n=int(input())
# for i in range(n,0,-1):
#   for j in range(1,n+1,1):
#     if j>i:
#       print('*',end='')
#     else:
#       print(j,end='')
#   for j in range(n,0,-1):
#     if j>i:
#       print('*',end='')
#     else:
#       print(j,end='')
#   print()
'''
ABCD
ABC
AB
A
'''

# n=int(input())
# for i in range(n,0,-1):
#   for j in range(0,i):
#       print(chr(65+j),end='')
#   print()
  
'''
4555
3455
2345
1234
'''
# n=int(input())
# for x in range(n,0,-1):
#   for y in range(x,n+1):
#     print(y,end='')
#   for z in range(0,x-1):
#     print(n+1,end='')
#   print()

'''
    1
   121
  12321
 1234321
  12321
   121
    1

'''
row=int(input('PLEASE ENTER ODD NUMBER OF ROWS: '))
c=row//2
for i in range(1,row+1):
    if i <= (row//2+1):
        for j in range(1,row+1-i):
            print(' ',end='')
        for j in range(1,i+1):
            print(j,end='')
        for j in range(i-1,0,-1):
            print(j,end='')
    else:
        for j in range(1,i):
            print(' ',end='')
        for j in range(1,c):
            print(j,end='')
        for j in range(c,0,-1):
            print(j,end='')
        c-=1
    print()
