# n = int(input("Enter the number of terms: "))
# sum = 0
# for i in range(1, n+1):
#     if i == 1:
#         sum += 1
#         print("1", end="")
#     else:
#         sum += 1/i
#         print(f"1/{i}", end="")
#     if i != n:
#         print(" + ", end="")
#     else:
#         print(" = ", end="")
# print(round(sum, 2))

# n = int(input("Enter the value of n: "))
# factorial = 1
# sum = 0
# for i in range(1, n+1):
#     factorial *= i
#     sum += i/factorial
# print(f"The sum of the series is {round(sum, 2)}")

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")

# n = int(input("Enter a decimal number: "))
# binary = ""
# while n > 0:
#     binary = str(n % 2) + binary
#     n //= 2
# print(f"The binary equivalent of {n} is {binary}")


# sentence = input("Enter a sentence: ")
# num_words = len(sentence.split())
# print(f"The number of words in the sentence is: {num_words}")

# import string

# sentence = input("Enter a sentence: ")
# num_punct = sum([1 for c in sentence if c in string.punctuation])
# print(f"The number of punctuation characters in the sentence is: {num_punct}")


'''
write a python program to print alphabet pattern 'A'.
Expected output:
 ***
*   *
*   *
*****
*   *
*   *
*   * 
'''
# for i in range(7):
#     for j in range(5):
#         if (i == 0 and j != 2) or (i == 3) or (i != 0 and i != 3 and j in [0, 4]):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

