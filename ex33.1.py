# i = 0
numbers = []
number_start = int(input("Введи начальное число: "))
number_finish = int(input("Введи последнее число: "))
step = int(input("Введи шаг: "))


def tick(number_start, number_finish, step):
    for i in range(number_start, number_finish + 1, step):
        print(f"В начале значение i равно {i}")
        numbers.append(i)

        print("Текущие значения: ", numbers)
        print(f"В конце значение i равно {i}")

tick(number_start, number_finish, step)
print("Значения: ")

for num in numbers:
    print(num)
