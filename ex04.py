#  присваиваем переменной cars целое значение 100
cars = 100
# присваиваем переменной space_in_a_car вещественное значение 4.0
space_in_a_car = 4.0
# присваиваем переменной drivers значение 30
drivers = 30
# присваиваем переменной passengers значение 90
passengers = 90
# значение переменной cars_not_driven есть разность переменных cars и drivers
cars_not_driven = cars - drivers
# присваиваем переменной cars_driven значение переменной drivers
cars_driven = drivers
# значение переменной carpool_capacity есть произведение двух других переменных
carpool_capacity = cars_driven * space_in_a_car
# значение переменной averange_passengers_per_car есть частное от деления
averange_passengers_per_car = passengers / cars_driven
# 1.в строке 8 python ссылается на переменную, которая не объявлена
# 2.чтобы найти ошибку и исправить имя переменной на правильную
print("В наличии", cars, "автомобилей.")
print("И только", drivers, "вышло на работу.")
print("Получается, что", cars_not_driven,"пустуют.")
print("Мы можем перевезти сегодня", carpool_capacity, "человек.")
print("Сегодня нужно отвезти", passengers, "человек.")
print("В каждой машине будет примерно", averange_passengers_per_car, "человека.")
