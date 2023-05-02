def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [3, 5, 2, 8, 1, 4]
print(bubble_sort(lst)) # [1, 2, 3, 4, 5, 8]
