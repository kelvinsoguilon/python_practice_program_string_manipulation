#ask user to input number from 0-1000
num = input("Enter a number from 0-1000: ")
#check if num is within range
if num.isdigit and 0 <= int(num) <= 1000:
#count how many 0 to add
    number_zeros = 6 - len(num)
    new_num = "0" * number_zeros + num
#print output