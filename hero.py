import random

class Hero:
    # Эти настройки (константы) потом можно вообще вынести в отдельный текстовый файл
    MIN_DMG = 1
    MAX_DMG = 7
    MAX_HEALTH = 15
    MAX_POTIONS = 3

    def __init__(self):
        self.health = self.MAX_HEALTH # здоровье
        self.potions = self.MAX_POTIONS # зелье

    def attack(self, dragon): # атаковать дракона
        receive_damage = dragon.receive_damage(self)
        print(f"Дракон получает {receive_damage} единиц урона.")

    def receive_damage(self, dragon): # получить урон от дракона
        dmg = random.randint(dragon.MIN_DMG, dragon.MAX_DMG)
        self.health -= dmg
        return dmg

    def drink_potion(self): # выпить зелье
        if self.potions <= 0:
            # эту проверку можно сделать в engine, чтобы игрок не мог пить зелья, если их нет
            return
        self.potions -= 1
        self.health += 5 # восстанавливаем 5 ед здоровья
