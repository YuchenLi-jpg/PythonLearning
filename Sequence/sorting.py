pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)  # return a list containing all the items in order
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key = str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael",
         ]
names.sort(key = str.casefold)  # in order
print(names)

