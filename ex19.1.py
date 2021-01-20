def my_best_func(tea_bags, cups):
    print(f"У нас в офисе есть {tea_bags} чайных пакетика и {cups} чашек.")

my_tea_bags = int(input("Enter number of your tea tea_bags:\n"))
some_plastic_cups = int(input("Enter number of plastic cups:\n"))

my_best_func(3, 5)
my_best_func(3, 3 + some_plastic_cups)
my_best_func(3 + my_tea_bags, 4 + some_plastic_cups)
my_best_func(3 + 5, 3 + 10)
my_best_func(my_tea_bags, some_plastic_cups)
