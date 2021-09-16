from sys import argv

script, input_file = argv

str = open(input_file)

print(str.readline(), end='')
print(str.readline(), end='')
print(str.readline(), end='')
str.seek(0)
print(str.readline(), end='')
