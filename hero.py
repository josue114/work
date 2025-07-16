# hero.py for hero profile
import random
class Hero:
    def __init__(self, batman, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = batman
        self.starting_health = starting_health
        self.current_health = starting_health
    def battle(self, opponent):
    # '''Fight another hero and randomly declare a winner'''
        self.opponent = opponent
        print(f"{self.name} battles {opponent}!")
        # Randomly choose winner
        winner = random.choice([self, opponent])
        print(f"{winner} wins the battle!") 
