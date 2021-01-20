def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print(f"Этого достаточно для вечеринки!")
    print("Погнали!\n")

# вызываем фунцию, в которую непосредственно передаем значения
print("Мы можем непосредственно передать числа функции:")
cheese_and_crackers(20, 30)

# присвоили значения переменным
print("ИЛИ, мы можем использовать переменные из нашего сценария:")
amount_of_cheese = 10
amount_of_crackers = 50
# и вызываем фунцию, передеав ей переменные
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# вызываем фунцию, внутри которой вычисляем значения
print("Мы даже можем выполнять вычисления внутри фунции:")
cheese_and_crackers(10 + 20, 5 + 6)

# вызываем функцю, внутри которой производятся вычисления с числами и переменными
print("И объединять переменные с вычислениями")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
