number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():   # check if it is numeric
        separators =separators + char

print(separators)