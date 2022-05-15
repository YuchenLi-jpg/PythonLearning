t = ("a", "b", "c")
print(t)
print()

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)  # a tuple containing 3 items.
# tuple is a sequence type, which means we could use indexing

# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# tuple is immutable
# Because they don't have the overhead of the methods needed to change them
# tuples use less memory than lists.
metallica2 = list(metallica)  # change tuple into a list
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

# Advantages of Tuples:
# 1. Using a tuple, for things that shouldn't change, can help to prevent
# bugs in your programs.
# 2. You can always unpack them successfully,because tuple is immutable
# you can always know how many items to be unpacked.

titles, artist, year = metallica
print(titles)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)     # unpack the tuple to a variable