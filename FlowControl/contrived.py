# numbers = [1, 45, 31, 16, 60]
# i = 0
# for number in numbers:
#     if number % 8 == 0:
#         # reject the list
#         print("The numbers are unacceptable")
#         break
#
# else:    # else is associated with for loop, not if
#     print("All those numbers are fine")


c = [-3, -4, -5, 5, 2, 1]
total = 0
for i in c:
    if i <= 0 :
        continue
    total += i
print(total)