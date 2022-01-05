class Hero:
    def __init__(self, health, potion):
        self.health = 5 # здоровье
        self.potion = 5 # зелье

    def attack(self): # атаковать дракона
        receive_damage = self.dragon.receive_damage()

    def drink_potion(self, potion): # выпить зелье
        self.potion -= 1

    def receive_damage(self, health): # получить урон от дракона
        self.health -= 1
