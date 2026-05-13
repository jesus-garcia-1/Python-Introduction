def remainders_5(numbers):
    return [number % 5 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9] # True
numbers_3 = [0, 5, 10] # False
numbers_4 = [] # True

print(all (remainders_5(numbers_1)), remainders_5(numbers_1))
print(all (remainders_5(numbers_2)), remainders_5(numbers_2))
print(all (remainders_5(numbers_3)), remainders_5(numbers_3))
print(all (remainders_5(numbers_4)), remainders_5(numbers_4))