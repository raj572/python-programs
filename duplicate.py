
# Taking user input 
arr = list(map(int, input("Enter the array elements : ").split()))

# Create an empty list
duplicate = [] 

# Iterate the array
for i in range(len(arr)): 
	# Check for duplicate item
	if arr[i] in arr[i + 1:]: 
		# add the item to the list if duplicate found
		duplicate.append(arr[i]) 

# Display the duplicate items
if (len(duplicate) > 0): 
	print("Duplicate items in the array : ", *duplicate) 
else: 
	print("No duplicate item found")