print("Today is a good day to learn python")
print('python is fun')
print("Python's string are easy to use")
print("We can even include 'quotes' in strings")
print("Hello " + "World")

greeting = "Hello"
# name = "Bruce"
name = input("Please enter your name ")
# name = "Tim"
print(greeting + name) # 这里不加引号是因为是variable
# if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

#data type
print(type(greeting))
print(type(age))
age = "2 years"
print(age)
print(type(age))

age_in_word = "2 years"
print(name + " is " + age_in_word + " years old")
#
# print(name + f" is {age} years old") # f strings
#
# # Integer & Float Data Types
# # integer data type is called int
# # floating point type is called float
#
# print(f"Pi is approximately {22 / 7:12.50f}")
# print(f"Pi is approximately {22 / 7:12.3f}")
#
# pi = 22 / 7
# print(f"Pi is approximately {pi:12.50f}")   # f strings 替换 format
#
