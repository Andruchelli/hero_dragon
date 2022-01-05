class Engine:
    def __init__(self):
        print("Добро пожаловать на игру \"Герой против Дракона\"")

    def next_turn(self, turn = 1):
        if turn % 2 != 0: # при нечётном числе ход за героем
            user = input("Выберите следующее действие: атаковать или пить зелье")
            if user == "атаковать":
                self.hero.attack()
            if user == "пить зелье":
                self.hero.drink_potion()

        else:
            self.dragon.attack()

        turn += 1

        if self.hero.health() == 0:
            print("Дракон победил")
        if self.dragon.health() == 0:
            print("Герой победил")
