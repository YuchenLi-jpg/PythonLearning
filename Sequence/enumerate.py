# for index, character in enumerate("abcdefgh"):
#     print(index, character)

# i = 0
# seq = ["one", "two", "three"]
# for j in seq:
#     print(i, seq[i])
#     i += 1
# # for i,j in enumerate(seq):
# #     print(i, j)

for t in enumerate("abcdefgh"):  # enumerate returns a tuple (i,j)
    index, character = t
    list = [index, character]
    all_list.append(list)
    print(all_list)

index, character = (0, 'a')
print(index)
print(character)
