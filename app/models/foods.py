from .templates import db, GameState
from .ants import Ant


class Food(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    x = db.Column(db.Integer())
    y = db.Column(db.Integer())
    value = db.Column(db.Integer())  # How many ants this will feed

    def __init__(self, world_id, x, y, value=1):
        self.world_id = world_id
        self.x = x
        self.y = y
        self.value = value

    @property
    def consumable(self):
        return True

    def consumed(self):
        self.value -= 1
        if self.value <= 0:
            self.world.remove_object(self)

