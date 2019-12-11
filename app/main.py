from random import randint

from flask import send_from_directory, jsonify

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest
from .models.users import User

from .serializers.ant_serializer import AntSerializer
from .serializers.colony_serializer import ColonySerializer

from .api.colony_controller import ColonyController
from .api.ant_controller import AntController
from .serializers.world_serializer import WorldSerializer

app = initialize(__name__, models=[World, Ant, Colony, Nest, User])


@app.route('/')
def root():
    return send_from_directory('dist', 'index.html')


@app.route('/grow')
def grow():
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony

    # colony.birth_ant()

    world.age += 1
    colony.move_ants()
    if randint(1, 100) > 15:
        colony.birth_ant()

    return jsonify(
        age=world.age,
        world=WorldSerializer.render(world)
    )


app.add_url_rule('/colony/<int:_id>', view_func=ColonyController.as_view('colony_controller'))

app.add_url_rule('/colony/<int:_id>', view_func=AntController.as_view('ant_controller'))




@app.route('/ant/<int:_id>')
def ant(_id):
    ant = Ant.query.get(_id)
    return jsonify(
        ant=AntSerializer.render(ant)
    )