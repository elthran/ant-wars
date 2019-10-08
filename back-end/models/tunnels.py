from templates import db, GameState


class Tunnel(GameState):
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'), nullable=False)
    x_pos = db.Column(db.Integer)
    y_pos = db.Column(db.Integer)

    def __init__(self, nest_id, x_pos, y_pos):
        self.nest_id = nest_id
        self.x_pos = x_pos
        self.y_pos = y_pos
