num = int(input())
def armstrong(num):
    x = num
    count = 0
    while x != 0:
        k = x % 10
        count += k*k*k
        x = x//10
    if count == num:
        print('true')
    else:
        print('false')
armstrong(num)