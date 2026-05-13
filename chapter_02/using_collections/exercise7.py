info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
my_string = info.split(':')
result = '+'.join(my_string)

result2 = info.replace(':', '+')

print(result)
print(result2)