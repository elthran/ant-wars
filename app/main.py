from random import randint
from time import sleep

from flask import Flask

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest

app = Flask(__name__.split('.')[0])
initialize(app, models=[World, Ant, Colony, Nest])

frame = 1


@app.route('/')
def main():
    global frame
    player1 = Colony.query.first()
    player1_nest = Nest.query.first()

    response = "Frame {frame}<br>".format(frame=frame)
    response += str(player1_nest)
    for ant in player1.ants:
        ant.move()
    frame += 1
    if randint(1, 100) > 100:
        player1.birth_ant()

    return response
