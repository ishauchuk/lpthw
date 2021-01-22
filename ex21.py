def add(a, b):
    print(f"СЛОЖЕНИЕ {a} + {b}")
    return a + b

def substract(a, b):
    print(f"ВЫЧИТАНИЕ {a} - {b}")
    return a- b

def multiply(a, b):
    print(f"УМНОЖЕНИЕ {a} * {b}")
    return a * b

def divide(a, b):
    print(f"ДЕЛЕНИЕ {a} / {b}")
    return a / b


print("Давайте выполним несколько вычислений с помощью функций!")

age = add(30, 5)
height = substract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)

print(f"Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}")


# Головоломка в качестве дополнительного задания, введи код в любом случае.
print("Это головоломка")
what = divide(iq, multiply(weight, substract(height, add(age, 2))))
simple_expression = age + height - weight * iq / 2
print("Получается: ", what, "Вы можете это вычислить вручную?")
print(simple_expression)
