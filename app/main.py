from random import randint
from time import sleep

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest


app = initialize(models=[World, Ant, Colony, Nest])


@app.route('/')
def main():
    frame = 1
    player1 = Colony.query.first()
    player1_nest = Nest.query.first()

    while True:
        print("Frame {frame}".format(frame=frame))
        print(player1_nest)
        print("\n\n\n")
        for ant in player1.ants:
            ant.move()
        frame += 1
        if randint(1, 100) > 100:
            player1.birth_ant()
        sleep(2)
