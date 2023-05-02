def insertionSort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
arr=[]
n=int(input("Enter how many elements do you want to sort :  "))
for i in range(n):
    val=int(input('Enter element : '))
    arr.append(val)
insertionSort(arr)
print(arr)
