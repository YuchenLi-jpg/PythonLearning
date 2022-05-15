# strings is one of sequence data type
#                   1
#         01234567890123
parrot = "Norwegian Blue"
#         43210987654321
#         1

print(parrot)
print(parrot[3])
print()
print(parrot[3] + "\n" + parrot[4] + "\n" + "\n" + parrot[3] + "\n" + parrot[6] + "\n" + parrot[8])
print()
print(parrot[-1]) # end of string start from -1
print(parrot[-14])
print("实验")
print(parrot[-11]+"\n"+parrot[-10]+"\n"+"\n"+parrot[-11]+"\n"+parrot[-8]+"\n"+parrot[-6])

print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14]) # 减去string的长度

parrot = "Norwegian Blue"
# slicing
print(parrot[0:6]) # Norweg, from index 0 to 5 (不包括6）
# up to but not including
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9]) # start from beginning of sequence
print(parrot[10:])
print(parrot[10:14])

print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl
print()
print(parrot[0:6])
print(parrot[-14:-8])

# steps
print(parrot[0:6:2]) # Nre
# The slice starts at index position 0
# It extends up to (but not including) position 6
# We step through the sequence in steps of 2
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])



