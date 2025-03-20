#ask user for fullname
fullname = input("Enter your fullname: ")
#store count of every character in fullname
character_count = 0
#check every character in input and adds it to count
for char in fullname:
    character_count += 1
#print result