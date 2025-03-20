#string input
full_name = ("Enter your name with leading spaces: ")
#variable to store new characters without space
fullname_without_space = ""
#space before text checker
space_found = True
#iterate every text character to identify spaces
for char in full_name:
    if char != " " or not space_found: #adds character that is not a space 
        fullname_without_space += char
        space_found = False 
#print output