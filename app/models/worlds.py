from .templates import db, GameState


class World(GameState):
    colonies = db.relationship('Colony', backref='world')
    age = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)

    def __init__(self):
        self.age = 0
        self.width = 50
        self.height = 50