name = 'Зед Шоу'
age = 35  # это правда!
height = 188  # см
weight = 80  #кг
eyes = 'Голубые'
teeth = 'Белые'
hair = 'Каштановые'
height_in_meters = height / 100
weight_in_tonns = weight / 1000

print(f"Давайте поговорим о челевеке по имени {name}.")
print(f"Его рост составляет {height_in_meters} м.")
print(f"Он весит {weight_in_tonns} т.")
print(f"На самом деле это не так много.")
print(f"У него {eyes} глаза и {hair} волосы.")
print(f"Его зубы обычно {teeth}, хотя он любит пить кофе.")
# эта строка кода сложная, не ошибитесь!
total = age + height_in_meters + weight_in_tonns
print(f"Если я сложу {age}, {height_in_meters} и {weight_in_tonns}, то получу {total}.")
