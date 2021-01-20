from sys import argv

script, input_file = argv
# описывается функция, которая печатает весь файл
def print_all(f):
    print(f.read())
# описывается функция, которая перемещает указатель текущей позиции в начало файла
def rewind(f):
    f.seek(0)
# функция, которая выодит строку и ее номер
def print_a_line(line_count, f):
    print(line_count, f.readline())
# происходит открытие файла и присваивание ей перменной
current_file = open(input_file)

print("Первым делом выведем этот файл целиком:\n")
# вызывается функция, которая полностью напечатает содержимое файла,
# полученного из командной строки
print_all(current_file)

print("Теперь отмотаем назада, словно это кассета.")
# вызывается функция, которая переместит указатель текущей позиции в начало файла
rewind(current_file)

print("Выведем три строки:")
# выводится первая строка файла
current_line = 1
print_a_line(current_line, current_file)
# выводится следующая строка файла
current_line += 1
print_a_line(current_line, current_file)
# и следующая
current_line += 1
print_a_line(current_line, current_file)
