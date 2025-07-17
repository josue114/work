import random

class Ability:
    def __init__(self, name, max_damage):
        self.max_damage = max_damage


def attack(self):
    '''returns a random interger between 0 and max_damage'''
    return random.radint(0, self.max_damage)

if __name__ == "__main__":
    fireball = Ability("fireball", 50)
    print(fireball.attack(0))
