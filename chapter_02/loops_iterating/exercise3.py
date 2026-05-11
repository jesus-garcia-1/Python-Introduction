# Use a while loop to print the numbers in my_list, one number per line. 
# Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

counter = len(my_list)
index = 0

while index < counter:
    print(my_list[index])
    index += 1

print('='*60)

for number in my_list:
    print(number)