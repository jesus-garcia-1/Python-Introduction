stuff = ('hello', 'world', 'bye', 'now')

my_list = list(stuff)
my_list[2] = 'goodbye'
stuff = tuple(my_list)

print(stuff)

stuff = ('hello', [3,2])
print(stuff)