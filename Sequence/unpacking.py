a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]  # data represents a list
data_list.append(15)
p, q, r = data_list  # would return error because too many items to be unpacked
print(p)
print(q)
print(r)

# we can unpack any sequence type.BUt lists are mutable

