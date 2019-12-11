from .templates import db, GameState
from .tunnels import Tunnel


class Nest(GameState):
    colony_id = db.Column(db.Integer, db.ForeignKey('colony.id'), nullable=False)
    entrance_x_pos = db.Column(db.Integer)  # Coordinates to entrance on the world map
    entrance_y_pos = db.Column(db.Integer)  # Coordinates to entrance on the world map

    def __init__(self, colony_id, entrance_x_pos, entrance_y_pos):
        self.colony_id = colony_id
        self.entrance_x_pos = entrance_x_pos
        self.entrance_y_pos = entrance_y_pos

    def get_colony(self):
        return
