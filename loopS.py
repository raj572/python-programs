'''
    1
   12
  123
 1234
'''
# n=int(input('Enter number of rows'))
# x=1
# while x<=n:
#     col=n+1
#     while col>=x:
#         print(' ',end='')
#         col-=1
#     z=1
#     while z<=x:
#         print(z,end='')
#         z+=1
#     print()
#     x+=1

n = int(input('Enter number of rows: '))

for x in range(1, n+1):
    for col in range(n, x-1, -1):
        print(' ', end='')
    for z in range(1, x+1):
        print(z, end='')
    print()

