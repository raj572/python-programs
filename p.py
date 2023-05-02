
# def check_split(arr):
#     sum_arr = sum(arr)
#     if sum_arr % 2 == 1:
#         return False
#     return split_array(arr, sum_arr // 2, 0)


# def split_array(arr, sum, i):
#     if sum == 0:
#         return True
#     if i == len(arr):
#         return False

#     if arr[i] % 5 == 0:
#         return split_array(arr, sum - arr[i], i + 1)
#     if arr[i] % 3 == 0:
#         return split_array(arr, sum - arr[i], i + 1)
#     return split_array(arr, sum, i + 1) or split_array(arr, sum - arr[i], i + 1)


# n = int(input())
# arr = [int(x) for x in input().split()]
# if check_split(arr):
#     print("true")
# else:
#     print("false")


# Python 3 implementation of the approach
 
# Recursive function that returns true if
# the array can be divided into two sub-arrays
# satisfying the given condition
def helper(arr, n, start, lsum, rsum):
 
    # If reached the end
    if (start == n):
        return lsum == rsum
 
    # If divisible by 5 then add
    # to the left sum
    if (arr[start] % 5 == 0):
        lsum += arr[start]
 
    # If divisible by 3 but not by 5
    # then add to the right sum
    elif (arr[start] % 3 == 0):
        rsum += arr[start]
 
    # Else it can be added to any of
    # the sub-arrays
    else:
 
        # Try adding in both the sub-arrays
        # (one by one) and check whether
        # the condition satisfies
        return (helper(arr, n, start + 1,
                lsum + arr[start], rsum) or
                helper(arr, n, start + 1,
                lsum, rsum + arr[start]));
 
    # For cases when element is multiple of 3 or 5.
    return helper(arr, n, start + 1, lsum, rsum)
 
# Function to start the recursive calls
def splitArray(arr, n):
     
    # Initially start, lsum and rsum
    # will all be 0
    return helper(arr, n, 0, 0, 0)
 
# Driver code
if __name__ == "__main__":
     
    n = int(input())
    arr = [int(x) for x in input().split()]
    if (splitArray(arr, n)):
        print("true")
    else:
        print("false")