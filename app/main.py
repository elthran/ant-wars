from random import randint
from time import sleep

from flask import render_template, send_from_directory, jsonify

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest

from .serializers.colony_serializer import ColonySerializer
from .serializers.ant_serializer import AntSerializer


app = initialize(__name__, models=[World, Ant, Colony, Nest])


@app.route('/')
def root():
    return send_from_directory('dist', 'index.html')


@app.route('/grow')
def grow():
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony
    nest = Nest.query.first()

    world.age += 1
    colony.move_ants()
    if randint(1, 100) > 100:
        colony.birth_ant()

    return jsonify(
        age=world.age,
        colony=colony,  # build serializer
        # colony=ColonySerializer.render(colony)
    )

@app.route('/colony/<int:id>')
def colony(id):
    colony = Colony.query.get(id)

    return jsonify(
        colony=ColonySerializer.render(colony)
    )


@app.route('/ant/<int:id>')
def ant(id):
    ant = Ant.query.get(id)

    return jsonify(
        colony=AntSerializer.render(ant)
    )