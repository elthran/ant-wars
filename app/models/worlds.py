import math
import random

from sqlalchemy.orm.collections import mapped_collection

from .maps import Map
from .foods import Food
from .pheromones import Pheromone
from .templates import db, GameState

import pdb


class World(GameState):
    """The world object which controls the game states for a player."""

    colonies = db.relationship('Colony', backref='world')
    """All colonies ('players') which exist in this world."""

    ants = db.relationship('Ant', backref='world')
    """All ants that exist in this world."""

    foods = db.relationship('Food', backref='world')
    """All foods which exist in this world."""

    age = db.Column(db.Integer)
    """How long this world has been running for."""

    width = db.Column(db.Integer)
    """The horizontal size of the world."""

    height = db.Column(db.Integer)
    """The vertical size of the world."""

    maps = db.relationship('Map', collection_class=mapped_collection(lambda _map: (_map.x,  _map.y)), backref='world')
    """The mapping of objects in the world to their coordinates."""

    pheromones = db.relationship('Pheromone',
                                 collection_class=mapped_collection(lambda _pheromone: (_pheromone.colony_id,
                                                                                        _pheromone.x,
                                                                                        _pheromone.y)),
                                 backref='world')
    """The mapping of pheromones in the world to their coordinates."""

    def __init__(self, width=50, height=50):
        self.age = 0
        self.width = width
        self.height = height

    def add_object(self, object_to_be_added):
        """Adds the object to this world.

        Args:
            object_to_be_added (Object): The object to be added to the world.
        """
        new_mapping = Map.add_object(self.id, object_to_be_added)
        if new_mapping:
            object_to_be_added.save()
            new_mapping.ref_id = object_to_be_added.id
            return True
        else:
            return False

    def remove_object(self, object_to_be_removed):
        """Removes the object from this world.

        Args:
            object_to_be_removed (Object): The object to be removed.
        """
        Map.remove_object(object_to_be_removed)
        object_to_be_removed.query.delete()

    def get_object_at_location(self, x, y):
        """Returns the object located at given coordinates.

        Args:
            x (int): X coordinate
            y (int): Y coordinates

        Returns:
            Object: The object located at those coordinates. None if nothing exists there.
        """
        object_map_at_target_location = self.maps.get((x, y))
        if not object_map_at_target_location:
            return None
        return object_map_at_target_location.get_real_object()

    def generate_food(self):
        """Creates a food object randomly somewhere in this world."""
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        new_food = Food(self.id, x, y)
        food_created = self.add_object(new_food)
        if not food_created:
            existing_object = self.get_object_at_location(x, y)
            if isinstance(existing_object, Food):
                existing_object.value += 1

    def add_pheromone_trail(self, colony_id, old_x, old_y, x, y):
        existing_trail = self.pheromones.get((colony_id, x, y))
        if not existing_trail:
            degrees = (math.degrees(math.atan2(old_y - y, old_x - x))) % 360
            new_trail = Pheromone.add_pheromone(self.id, 1, x, y, 'food-path', degrees, 1)
        elif existing_trail.colony_id == 1:
            existing_trail.strength += 1
