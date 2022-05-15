for i in range(1, 13):            # align space
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
               # space 2
print()
for i in range(1, 13):            # left align space
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
                                                       # 居中
print()
print("Pi is approximate {0:12}".format(22 /7))
print("Pi is approximate {0:12f}".format(22 /7))
print("Pi is approximate {0:12.50f}".format(22 /7))
print("Pi is approximate {0:52.50f}".format(22 /7))
print("Pi is approximate {0:62.50f}".format(22 /7))
print("Pi is approximate {0:<72.50f}".format(22 /7))
print("Pi is approximate {0:<72.51f}".format(22 /7))
                            # left align

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

for i in range(1, 13):
    print(f"No. {i} squared is {i**2} and cubed is {i**3:4}")