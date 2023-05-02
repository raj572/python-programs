row = int(input()) #Number of rows
col = int(input()) #Number of columns
inputL= input().split() #Converting input string to list
fnlList=[[int(inputL[i*col+j]) for j in range(col)] for i in range(row)]
print(fnlList)
