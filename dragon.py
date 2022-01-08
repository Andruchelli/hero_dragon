import random

class Dragon:
    MIN_DMG = 0
    MAX_DMG = 9
    MAX_HEALTH = 20

    def __init__(self):
        self.health = self.MAX_HEALTH # здоровье

    def attack(self, hero): # атаковать героя
        receive_damage = hero.receive_damage(self)
        print(f"Герой получает {receive_damage} единиц урона.")

    def receive_damage(self, hero): # получить урон от героя
        dmg = random.randint(hero.MIN_DMG, hero.MAX_DMG)
        self.health -= dmg
        return dmg

