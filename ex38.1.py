cities = ["Minsk", "Brest", "Grodno", "Vitebsk", "Mogilev", "Gomel"]

your_city = input("Enter your living place: ")

if your_city in cities:
    print(f"{your_city} is the best.")
    if your_city == "Minsk":
        print("ooohhh, it is the capital of Belarus.")
else:
    print("You are living in the village.")
    cities.append(your_city)

print("New list of cities is:")
print(*cities, sep=', ')
cities.sort()
print("Sorted list by alphabet:")
print(*cities, sep=', ')
print("Number of cities :", len(cities))
