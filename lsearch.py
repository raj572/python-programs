a=[1,2,4,3,9,0,5]
x=int(input())
n=len(a)
#linear search
for i in range(n):
    if i>n:
        print('not found')
    if a[i]==x:
        print('found')
    i+=1
#binary search 
low=a[0]
high=a[n-1]
while low<=high:
    if x not in a:
        print('not found')
        break
    mid=low+high
    if x==a[mid]:
        print('true')
        break
    elif x>a[mid]:
        low=mid+1
    else:
        high=mid-1
