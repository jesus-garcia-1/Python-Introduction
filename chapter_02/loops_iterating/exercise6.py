my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

my_list2 = []
for number in my_list:
    if number % 2 == 0:
        my_list2.append('even')
    
    else:
        my_list2.append('odd')

print(my_list2)