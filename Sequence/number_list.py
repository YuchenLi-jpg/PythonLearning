even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
another_even = even
print(another_even)
print(id(even))

even.sort(reverse= True)  # sort method doesn't create a copy of the list- it rearranges the items in the list
print(even)
print(id(even))
print(another_even)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("issi"))


