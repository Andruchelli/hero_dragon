from hero import superhero as hr
from dragon import drakon as dr

class Engine():
    def __init__(self):
        print("Добро пожаловать на игру \"Герой против Дракона\"")

    def next_turn(self, turn = 1):
        if turn % 2 != 0: # при нечётном числе ход за героем
            user = input("Выберите следующее действие: атаковать или пить зелье: ")
            if user == "атаковать":
                hr.attack()
            if user == "пить зелье":
                hr.drink_potion()

        else:
            dr.attack()

        turn += 1

        if hr.health() == 0:
            print("Дракон победил")
        if dr.health() == 0:
            print("Герой победил")
