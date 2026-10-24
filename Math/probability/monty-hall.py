"""
The Monty Hall problem is a brain-teaser, in the form of a probability puzzle,
loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall.

Suppose you're on a game show, and you're given the choice of three doors:
    Behind one door is a car;
    behind the others, goats.
You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, "Do you want to pick door No. 2?"
Is it to your advantage to switch your choice?

Vos Savant's response was that the contestant should switch to the other door.
Under the standard assumptions, the switching strategy has a 2/3 probability of winning the car,
while the strategy that remains with the initial choice has only a 1/3 probability.

Let's simulate the game.
"""

from random import randrange


class MontyHallGame:
    """
    Monty-Hall game class.
    Randomly sets a car behind 3 doors.
    Picks a random door.
    Evaluates the result:
        0 - Picked a door with the goat. Switch wins a car.
        1 - Picked a door with a car switch looses a game.
    """

    def __init__(self):
        self.car = randrange(0, 3)
        self.picked, self.result = None, None

    def pick_door(self):
        """
        Pick one of 3 the doors.
        """
        self.picked = randrange(0, 3)

    def open_another(self):
        """
        No actual door open is needed. Two cases here:
            1.  Player already picked a door with the car. We open (remove from consideration) any door with a goat.
                In this case switch always looses.
            2.  Player picked a door with a goat. Then we open (remove from consideration) the second door with a goat.
                In this case switch always wins.
        Evaluating the result.
        """
        self.result = 1 if self.picked == self.car else 0

    def get_result(self):
        if self.result is None:
            raise Exception(f"No result at the time. First pick a door and open one with a goat")
        return self.result


if __name__ == "__main__":
    """
    res dictionary stores counts of 2 game results:
        0 - Picked a door with the goat. Switch wins a car.
        1 - Picked a door with a car. Switch looses a game.
    """

    NUMBER_OF_GAMES = 1_000_000
    res = {0: 0, 1: 0}
    for _ in range(NUMBER_OF_GAMES):
        game = MontyHallGame()
        game.pick_door()
        game.open_another()
        res[game.get_result()] += 1

    switch_win_prob = res[0] / NUMBER_OF_GAMES
    switch_loose_prob = res[1] / NUMBER_OF_GAMES

    print(f"---> {NUMBER_OF_GAMES} games played")
    print(f"---> Switch strategy wins in {round(switch_win_prob * 100, 2)} % games")
    print(f"---> Switch is {round(switch_win_prob / switch_loose_prob, 4)} times more preferable")
