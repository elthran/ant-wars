from random import randint

from flask import send_from_directory, jsonify

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest
from .models.users import User

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

    world.age += 1
    colony.move_ants()

    if randint(1, 100) > 95:
        colony.birth_ant()

    return jsonify(
        age=world.age,
        world=WorldSerializer.render(world)
    )


app.add_url_rule('/colony/<int:_id>', view_func=ColonyController.as_view('colony_controller'))

app.add_url_rule('/colony/<int:_id>', view_func=AntController.as_view('ant_controller'))


@app.route('/change_colony_goal/<string:new_goal>')
def change_colony_goal(new_goal):
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony
    colony.update_goal(new_goal)
    return jsonify(
        age=world.age,
        world=WorldSerializer.render(world)
    )


@app.route('/dig_nest')
def dig_nest():
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony
    if len(colony.nests) == 0:
        nest = Nest(colony.id, world.height // 2, world.width // 2)
        nest.save()
    return jsonify(
        age=world.age,
        world=WorldSerializer.render(world)
    )
