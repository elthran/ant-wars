import random

from sqlalchemy.orm.collections import mapped_collection

from .maps import Map
from .foods import Food
from .templates import db, GameState


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

    def add_object(self, _object):
        if self.maps.get((_object.x_pos, _object.y_pos)) is None:
            new_map = Map(self.id, _object.x_pos, _object.y_pos, "ant_guy")
            new_map.save()
        else:
            print("conflict at:", _object.x_pos, _object.y_pos)
        # self.maps[(_object.x_pos, _object.y_pos)] = _object

    def generate_food(self):
        x_pos = random.randint(0, self.width)
        y_pos = random.randint(0, self.height)
        new_food = Food(self.id, x_pos, y_pos)
        new_food.save()
        self.add_object(new_food)

    def get_object_at_location(self, x_pos, y_pos):
        for food in self.foods:
            if food.x_pos == x_pos and food.y_pos == y_pos:
                return food
        for colony in self.colonies:
            for ant in colony.ants:
                if ant.x_pos == x_pos and ant.y_pos == y_pos:
                    return ant
        return None

    def move(self, _object, x_pos, y_pos):
        object_moved_into = self.get_object_at_location(x_pos, y_pos)
