def is_palindromes(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindromes(word):
    print(" '{}' is a palindrome".format(word))
else:
    print(" '{}' is not a palindromes".format(word))

# def sum_eo(n, t):
#     even = 0
#     odd = 0
#     if t == "e":
#         for number in range(1, n+1):
#             if 2 * number < n:
#                 even += 2 * number
#         return even
#     elif t == "o":
#         for number in range(1, n):
#             if number % 2 == 1:
#                 odd += number
#         return odd
#     else:
#         return -1



# def sum_eo(n, t):
#     """Sum even or odd numbers in range.
#
#     Return the sum of even or odd natural numbers, in the range 1..n-1.
#
#     :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
#     :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
#     :return: The sum of the even or odd numbers in the range.
#             Returns -1 if `t` is not 'e' or 'o'.
#     """
#     if t == "e":
#         start = 2
#     elif t == 'o':
#         start = 1
#     else:
#         return -1
#
#     return sum(range(start, n, 2))
#
#
# x = sum_eo(11, 'spam')
# print(x)






