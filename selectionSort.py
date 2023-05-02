def selectionSort(nums):
    l=len(nums)
    for i in range(l-1):
        minpos=i
        for j in range(i,l):
            if nums[j]<nums[minpos]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]
# creating an empty list
nums = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	nums.append(ele) # adding the element

selectionSort(nums)
print(nums)
