from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    temp=0
    for i in range(1,n,2):
        j=i-1
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j=j+2
    
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1