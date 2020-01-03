import random

from flask import render_template, send_from_directory, jsonify

from .config.initialize import initialize

from .models.worlds import World
from .models.ants import Ant
from .models.colonies import Colony
from .models.nests import Nest
from .models.users import User
from .models.maps import Map

from .blueprints.api_blueprint import api_blueprint
from .serializers.world_serializer import WorldSerializer

app = initialize(__name__, models=[World, Map, Ant, Colony, Nest, User])

app.register_blueprint(api_blueprint)

@app.route('/')
def root():
    """Currently the 'main' function. Runs the world each time page is refreshed.

    Returns:
        JSONIFY: A serialized view of the world state.
    """
    return send_from_directory('dist', 'index.html')


@app.route('/grow')
def grow():
    world = World.query.first()
    colonies = Colony.query.all()

    world.age += 1
    if random.randint(1, 10) < 8:
        world.generate_food()

    for colony in colonies:
        colony.advance_time()

    return jsonify(
        world=WorldSerializer.render(world)
    )


@app.route('/change_colony_goal/<string:new_goal>')
def change_colony_goal(new_goal):
    """Tells the user's colony to update its goal.

    Args:
        new_goal (str): The new colony goal.

    Returns:
        JSONIFY: A serialized view of the world state.
    """
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony
    colony.update_goal(new_goal)
    return jsonify(
        world=WorldSerializer.render(world)
    )


@app.route('/dig_nest')
def dig_nest():
    """Tells the user's colony to dig a nest.

    Returns:
        JSONIFY: A serialized view of the world state.
    """
    world = World.query.first()
    colony = Colony.query.first()  # current_user.colony
    if len(colony.nests) == 0:
        nest = Nest(colony.id, world.height // 2, world.width // 2)
        nest.save()
    return jsonify(
        world=WorldSerializer.render(world)
    )
