# # Take input from user
# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))

# # Create a two dimensional list
# two_dimensional_list = [[0 for j in range(columns)] for i in range(rows)]

# # Take input from user
# for i in range(rows):
#     for j in range(columns):
#         two_dimensional_list[i][j] = int(input("Enter an element: "))

# # Print the two dimensional list
# for i in range(rows):
#     for j in range(columns):
#         print(two_dimensional_list[i][j], end=" ")
#     print()



# def create_list():
#     """
#     Create a two dimensional list
#     """
#     row = int(input("Enter number of rows: "))
#     col: int = int(input("Enter number of columns: "))
#     lst = []
#     for i in range(row):
#         lst.append([])
#         for j in range(col):
#             lst[i].append(int(input("Enter element: ")))
#     return lst

# def main():
#     """
#     Main function
#     """
#     lst = create_list()
#     print(lst)

# if __name__ == '__main__':
#     main()

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()