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


@app.route('/')
def grow():
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony
    nest = Nest.query.first()

    world.age += 1
    colony.move_ants()
    if randint(1, 100) > 100:
        colony.birth_ant()

    response = "Frame {frame}<br>".format(frame=world.age)
    response += str(nest).replace('\n', '<br>')  # maybe a template ... or json

    return response
