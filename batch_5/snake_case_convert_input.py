#ask user for name in incorrect casing
fullname = input("Enter your name in incorrect casing: ")
#convert characters to lowercase
lowercased_fullname = fullname.lower()
#change spaces to underscore
snake_case = lowercased_fullname.replace(" ", "_")
#print result