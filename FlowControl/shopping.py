shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue  # cause everything in the loop to be ignored
#
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)
