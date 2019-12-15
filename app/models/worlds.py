import random

from sqlalchemy.orm.collections import mapped_collection

from .maps import Map
from .foods import Food
from .templates import db, GameState

import pdb


class World(GameState):
    colonies = db.relationship('Colony', backref='world')
    ants = db.relationship('Ant', backref='world')
    foods = db.relationship('Food', backref='world')
    age = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    maps = db.relationship('Map',
                           collection_class=mapped_collection(lambda _map: (_map.x_pos,
                                                                            _map.y_pos)),
                           backref='world')

    def __init__(self):
        self.age = 0
        self.width = 50
        self.height = 50

    def move(self, old_x, old_y, new_x, new_y):
        object_at_location = Map.get_object_at_location(new_x, new_y)
        if object_at_location:
            return object_at_location

    def add_object(self, object_to_be_added):
        new_mapping = Map.add_object(self.id, object_to_be_added)
        if new_mapping:
            object_to_be_added.save()
            new_mapping.ref_id = object_to_be_added.id

    def remove_object(self, object_to_be_removed):
        Map.remove_object(object_to_be_removed)
        object_to_be_removed.query.delete()

    def get_object_at_location(self, x_pos, y_pos):
        """
        Before an object moves, it should request to see what exists in the new location.
        """
        object_map_at_target_location = self.maps.get((x_pos, y_pos))
        if not object_map_at_target_location:
            return None
        return object_map_at_target_location.get_real_object()

    def generate_food(self):
        x_pos = random.randint(0, self.width)
        y_pos = random.randint(0, self.height)
        new_food = Food(self.id, x_pos, y_pos)
        self.add_object(new_food)
