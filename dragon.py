class Dragon:
    def __init__(self, health):
        self.health = 5 # здоровье

    def attack(self): # атаковать героя
        receive_damage = self.hero.receive_damage()

    def receive_damage(self, health): # получить урон от героя
        self.health -= 1
