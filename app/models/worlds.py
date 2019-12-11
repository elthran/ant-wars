import random

from .foods import Food
from .templates import db, GameState


class World(GameState):
    colonies = db.relationship('Colony', backref='world')
    foods = db.relationship('Food', backref='world')
    age = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)

    def __init__(self):
        self.age = 0
        self.width = 50
        self.height = 50

    def generate_food(self):
        x_pos = random.randint(0, self.width)
        y_pos = random.randint(0, self.height)
        new_food = Food(self.id, x_pos, y_pos)
        self.foods.append(new_food)

    def get_object_at_location(self, x_pos, y_pos):
        for food in self.foods:
            if food.x_pos == x_pos and food.y_pos == y_pos:
                return food
        for colony in self.colonies:
            for ant in colony.ants:
                if ant.x_pos == x_pos and ant.y_pos == y_pos:
                    return ant
        return None
