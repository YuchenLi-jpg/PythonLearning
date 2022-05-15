letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]   # Negative step: start index > stop index
print(backwards)

print(letters[25::-1])
# or
print(letters[::-1])

print(letters[16:13:-1]+" "+letters[4::-1]+" "+letters[:-9:-1])

# Create a slice produces the characters qpo
print(letters[16:13:-1])  # Slice back 前面的ｉｎｄｅｘ　倒着来
# Slice the string to product edcba
print(letters[4::-1])
# Slice the string to produce the last 8 characters, in reverse order
print(letters[25:17:-1])
print(letters[:-9:-1])


print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[:])

# Sequence of list is ordered

