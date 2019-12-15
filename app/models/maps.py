from .templates import db, GameState, Template
from .ants import Ant


class Map(Template):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    x_pos = db.Column(db.Integer, primary_key=True, nullable=False)
    y_pos = db.Column(db.Integer, primary_key=True, nullable=False)
    object_and_id = db.Column(db.String(30))  # How many ants this will feed

    def __init__(self, world_id, x_pos, y_pos, object_and_id):
        self.world_id = world_id
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.object_and_id = object_and_id

