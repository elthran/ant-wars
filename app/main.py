from random import randint
from time import sleep

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # pip install Flask-SQLAlchemy

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest


app = Flask(__name__)

flask_db = SQLAlchemy()

flask_db.init_app(app)

db = flask_db



def run_game():
    # Initialize
    frame = 1
    game_world = World()
    game_world.save()
    player1 = Colony(game_world.id)
    player1.save()
    player1_nest = Nest(player1.id, 25, 25)
    player1_nest.save()
    player1_ant = Ant(player1.id, player1_nest.id, 20, 20)
    player1_ant.save()
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


run_game()
