#ask user for fullname
fullname = input("Enter your name in incorrect casing: ")
#split name into words
name_parts = fullname.split()
#capitalize only first letter of the word
capitalized_letter = [word.capitalize() for word in name_parts]
#put words back in a single string
proper_casing = " ".join(capitalized_letter)
#print output
print(proper_casing)