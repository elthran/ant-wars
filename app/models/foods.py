from .templates import db, GameState
from .ants import Ant


class Food(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    x_pos = db.Column(db.Integer())
    y_pos = db.Column(db.Integer())
    value = db.Column(db.Integer())  # How many ants this will feed

    def __init__(self, world_id, x_pos, y_pos, value=1):
        self.world_id = world_id
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value

    def consumed(self):
        self.world.remove_object(self)

