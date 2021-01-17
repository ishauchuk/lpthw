age = input("Сколько тебе лет?\n")
print("Каков твой рост?", end=' ')
height = int(input())
print("Сколько ты весишь?", end=' ')
weight = int(input())
hair_color = input("Каков твой цвет волос?\n")

print(f"Итак, тебе {age} лет, в тебе {height} см роста,\
 {weight} кг веса, у тебя {hair_color} волосы. ")
print(type(age), type(height), type(weight))
