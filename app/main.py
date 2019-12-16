import random

from flask import send_from_directory, jsonify

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest
from .models.users import User
from .models.maps import Map

from .api.colony_controller import ColonyController
from .api.ant_controller import AntController
from .serializers.world_serializer import WorldSerializer

app = initialize(__name__, models=[World, Map, Ant, Colony, Nest, User])


@app.route('/')
def root():
    world = World.query.first()
    colonies = Colony.query.all()

    world.age += 1
    if random.randint(1, 10) < 11:
        world.generate_food()

    for colony in colonies:
        colony.advance_time()

    return jsonify(
        age=world.age,
        world=WorldSerializer.render(world)
    )


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


@app.route('/old_stuff')
def old_stuff():
    return send_from_directory('dist', 'index.html')


app.add_url_rule('/colony/<int:_id>', view_func=ColonyController.as_view('colony_controller'))

app.add_url_rule('/colony/<int:_id>', view_func=AntController.as_view('ant_controller'))
