# Write a Python class called Dice, which represents a set of playing dice. The constrictor of this class should get
# as arguments the number of dice in the set and the number of sides in these dice (a standard dice have 6 sides, but
# dice with more sides do exist). The class should provide a function Roll() that returns a list of numbers that
# represent a roll of the dice.

import random

class Dice:
    def __init__(self, num_dice=1, sides=6):
        self.num_dice = num_dice
        self.sides = sides
    def Roll(self):
        roll_list = []
        for i in range(self.num_dice):
            roll_val = random.randint(1,self.sides)
            roll_list.append(roll_val)
        return roll_list

craps_dice = Dice(2,6)

print craps_dice.Roll()
