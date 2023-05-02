import numpy as np

# # create a 2D NumPy array
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# # calculate the sum of each row
# row_sums = arr.sum(axis=1)
# print("Row sums:", row_sums)

# # calculate the sum of each column
# column_sums = arr.sum(axis=0)
# print("Column sums:", column_sums)

'''# create a 2D NumPy array of size 5x5 with ones on the diagonal and zeros everywhere else
import numpy as np

# create a 5x5 array with all zeros
arr = np.zeros((5, 5))

# set diagonal elements to ones
np.fill_diagonal(arr, 1)

# print the array without dot
np.set_printoptions(formatter={'float_kind':'{:0}'.format})
print(arr)'''


# import numpy as np

# # create a 1D array with some repeated values
# arr = np.array([1, 2, 3, 2, 3, 3, 4, 5, 1])

# # find the unique values and their counts
# unique, counts = np.unique(arr, return_counts=True)

# # print the results
# for i in range(len(unique)):
#     print("Value", unique[i], "appears", counts[i], "time(s)")


'''
import numpy as np

# create a 2D array
arr = np.array([[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7],
                [2, 4, 6],
                [5, 3, 1]])

# get the indices that would sort the first column
sort_indices = np.argsort(arr[:, 0])

# use the indices to sort the entire array
sorted_arr = arr[sort_indices]

# print the sorted array
print(sorted_arr)
'''

# import numpy as np

# # create a 1D array with some values
# arr = np.array([2, 5, 10, 12, 8, 15, 3])

# # replace values greater than 10 with 10
# arr = np.where(arr > 10, 10, arr)

# # print the resulting array
# print(arr)

import numpy as np

array = np.random.randint(0, 10, size=(5, 3))
print(array)

