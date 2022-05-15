activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

# str.casefold() Return a casefolded copy of the string. may be used
# for caseless matching