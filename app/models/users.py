from .templates import db, GameState
from .ants import Ant


class User(GameState):
    colonies = db.relationship('Colony', backref='user')
    username = db.Column(db.String(32))

    def __init__(self, username):
        self.username = username
