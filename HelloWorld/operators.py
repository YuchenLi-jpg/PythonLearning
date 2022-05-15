a = 12 # bind variable to values
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0 # float result
print(a // b) # 4 integer division, rounded down towards miuns infinity
print(a % b)# 0 modulo: the remainder after integer division

print()

# range(1, 4) is also an expression
for i in range(1, a // 4):
    print(i)  # i is an expression, i is to be

print(a + b / 3 - 4 * 12)
# higher precedence in * and /
print(a + (b / 3) - (4 * 12))
print((((a +b)/3)-4)*12)

c = a + b
d = c / 3
e = d -4
print(e * 12)

print()
print(a / (b *a) / b)

