n=int(input())
row=1
while row<=n:
    col=1
    while col<=row:
        print('*',end=' ')
        col+=1
    print()
    row+=1
# for i in range(n+2):
#     for j in range(1,i):
#         print(j,end='')
#     print()
'''
1
12
123
1234
'''