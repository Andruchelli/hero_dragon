from hero import superhero as hr

class Dragon:
    def __init__(self, health):
        self.health = 5 # здоровье

    def attack(self): # атаковать героя
        receive_damage = hr.receive_damage()

    def receive_damage(self, health = 5): # получить урон от героя
        self.health -= 1
drakon = Dragon()
