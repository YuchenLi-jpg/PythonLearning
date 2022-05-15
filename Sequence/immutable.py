# indexing and slicing works the same with a list as it did with a string
# because they are both sequence types.

# immutable types:  int, float, bool,str, tuple, frozenset, bytes
# cannot be changed themselves

# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))