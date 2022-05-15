# 我得方法
# def is_palindromes(sentence):
#     vocabulary = "abcdefghijklmnopqrstuvwxyz"
#     string = []
#     for i in sentence.casefold():
#         if i in vocabulary:
#             string.append(i)
#             print(string)
#     return string[::-1] == string
#
#
# sentence = input("Please enter a sentence to check: ")
# if is_palindromes(sentence):
#     print(" '{}' is a palindrome".format(sentence))
# else:
#     print(" '{}' is not a palindromes".format(sentence))

def is_palindromes(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():   # check whether a single character is a word/numbers
            string += char   # isalnum() return True if all character is word/numbers

    # return string[::-1].casefold() == string.casefold()
    return is_palindromes(string)


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print(" '{}' is a palindrome".format(word))
else:
    print(" '{}' is not a palindromes".format(word))
