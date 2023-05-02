def segregate_01(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0:
            left += 1
        while arr[right] == 1:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

n=input('Enter 0 and 1 : ')
arr = n.split()
print(segregate_01(arr))