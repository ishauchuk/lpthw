class Song(object):

    def __init__(self, lyrics, group_and_song):
        self.lyrics = lyrics
        self.group_and_song = group_and_song

    def sing_me_a_sing(self):
        print(self.group_and_song)
        for line in self.lyrics:
            print(line)

happy_bday = ["В этот день родили меня на свет,",
                    "В этот день с иголочки я одет,",
                    "В этот день теплом вашим я согрет:",
                    "Мне сегодня 30 лет!"]

bulls_on_parade = Song(["Как бессонница в час ночной,",
                        "Меняет, нелюдимая, облик твой,",
                        "Чьих невольница ты идей?",
                        "Зачем тебе охотиться на людей?"],
                        "'КИШ - Кукла колдуна'")

Song(happy_bday, "'Сектор Газа - 30 лет'").sing_me_a_sing()
print('*' * 10)
bulls_on_parade.sing_me_a_sing()
