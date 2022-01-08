from hero import Hero
from dragon import Dragon

class Engine():
    def __init__(self):
        print("Добро пожаловать на игру \"Герой против Дракона\"")
        self.hero = Hero()
        self.dragon = Dragon()

    def next_turn(self, turn = 1):
        if turn % 2 != 0: # при нечётном числе ход за героем
            action = input("Выберите следующее действие: атаковать или пить зелье: ")
            # в идеале здесь нужно сделать проверку ввода, чтобы игрок не пытался ввести несуществующее действие
            if action == "атаковать":
                self.hero.attack(self.dragon)
            if action == "пить зелье":
                self.hero.drink_potion()

        else:
            self.dragon.attack(self.hero)

        

        if self.hero.health <= 0:
            print(f"Дракон победил на {turn} ходу")
            return
        if self.dragon.health <= 0:
            print(f"Герой победил на {turn} ходу")
            return
        
        print("\n===========")
        print(f"Здоровье героя: {self.hero.health}")
        print(f"Зелий осталось: {self.hero.potions}")
        print(f"Здоровье дракона: {self.dragon.health}")
        self.next_turn(turn + 1)
