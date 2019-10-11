from .templates import db, GameState


class World(GameState):
    colonies = db.relationship('Colony', backref='world')
    age = db.Column(db.Integer, default=0)
