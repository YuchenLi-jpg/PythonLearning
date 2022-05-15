data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here 开发的办法一
for i, j in enumerate(data):
    if i in [1, 2, 3, 4, 5, 7, 13, 14, 15, 16, 17]:
        flowers.append(j)
    else:
        shrubs.append(j)
print(flowers)
print(shrubs)

#开发的办法二
# for index in range(len(data)):
#     if "Flower" in data[index]:
#         flowers.append(data[index])
#     else:
#         shrubs.append(data[index])
#
# print(flowers)
# print(shrubs)