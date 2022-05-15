panagram = """The quick brown 
fox jumps\tover
the lazy dog"""

words = panagram.split()   # split() return the list. It returns all the items in the string that
                            # separate by one or more white space(default)
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = ["9", " ",
                  "2", "2", "3", " ",
                  "3", "7", "2", " ",
                  "0", "3", "6", " ",
                  "8", "5", "4", " ",
                  "7", "7", "5", " ",
                  "8", "0", "7"]

values = "".join(generated_list)  # join create a string
print(values)
values_list = values.split()  # split creates a list
print(values_list)

# 我的办法：(同时也是老师的办法2）
int_list = []
for item in values_list:
    int_list.append(int(item))

print(int_list)
# 老师的办法：
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)




