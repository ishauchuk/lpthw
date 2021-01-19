from sys import argv

script, filename = argv
txt = open(filename)
print(f"Сейчас будет открыт файл {filename}")

print("Открываю и читаю файл...")
print(txt.read())
txt.close()
