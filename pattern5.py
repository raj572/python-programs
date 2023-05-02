'''
   1
  121
 12321
  121
   1
'''
n=int(input())
row=1
while row<=n:
    spaces=1
    while spaces<=n-row:
        print(' ',end='')
        spaces=spaces+1
    num=1
    while num<=row:
        print(num,end='')
        num+=1
    num=row-1
    while num>=1:
        print(num,end='')
        num-=1
    print()
    row+=1
for row in range(n,0,-1):
    for spaces in range(row,n):
        print(' ',end='')
    for num in range(1,row):
        print(num,end='')
    print()
    
