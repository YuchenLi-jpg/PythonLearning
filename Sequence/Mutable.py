shopping_list = ["milk",
                 "pasta"
                 "spam"
                 "bread"
                 "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
print()
list = shopping_list.copy()  # 产生一个全新的list   .copy()
print(id(list))

shopping_list += ["cookies"]
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)
