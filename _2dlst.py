col=int(input("Enter column number : "))
row=int(input("Enter row number : "))
list=[[int(input("Enter element : ")) for i in range(col)]for j in range(row) ]
for r in list:
    for c in r:
        print(c,end=' ')
    print()

