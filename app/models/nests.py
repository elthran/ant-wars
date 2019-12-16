from .templates import db, GameState


class Nest(GameState):
    colony_id = db.Column(db.Integer, db.ForeignKey('colony.id'), nullable=False)
    entrance_x = db.Column(db.Integer)  # Coordinates to entrance on the world map
    entrance_y = db.Column(db.Integer)  # Coordinates to entrance on the world map

    def __init__(self, colony_id, entrance_x, entrance_y):
        self.colony_id = colony_id
        self.entrance_x = entrance_x
        self.entrance_y = entrance_y

    def get_colony(self):
        return
