#ask user for full name
fullname = input("Enter your name in incorrect casing: ")
#reverse case of each letter
reversed_case = [char.upper() if char.islower() else char.lower() for char in fullname]
#join words into one string
fullname_reversed = "".join(reversed_case)
#print result
print(fullname_reversed)