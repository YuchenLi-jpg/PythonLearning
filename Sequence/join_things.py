flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

separator = ", "
output = separator.join(flowers)  # join is a method of str (must be str)
print(output)

print(", ".join(flowers))

print(output.split(','))
