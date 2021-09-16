class MyStuff(object):

    def __init__(self):
        self.tangerine = "Пусть бегут неуклюже..."

    def apple(self):
        print("Я - САМОЕ СЛАДКОЕ ЯБЛОКО!")

thing = MyStuff()
thing.apple()
# print(thing.tangerine)
print(MyStuff().tangerine)
MyStuff().apple()

# import mystuff
# mystuff.apple()
# print(mystuff.tangerine)
