from random import randint


class Die:
    """Simulate a dice"""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, times=1):
        """Simulate a 6 sided dice roll."""
        for ignored in range(times):
            print(randint(1, self.sides))


dice1 = Die(6)
dice2 = Die(10)
dice3 = Die(20)

#dice1.roll_die(5)
#dice2.roll_die(10)
dice3.roll_die(10)
