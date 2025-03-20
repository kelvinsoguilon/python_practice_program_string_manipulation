#ask user for fullname
fullname = input("Enter your name in incorrect casing: ")
#store characters in variable
pascal_case = ""
#split the string into words
capitalized_letter = fullname.split()
#capitalize the first letters of each word
proper_case = [word.capitalize() for word in capitalized_letter]
#remove the spaces
for char in proper_case:
    if char != " ":
        pascal_case += char
#print result in pascal casing
print(pascal_case)