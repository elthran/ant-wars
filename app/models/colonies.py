from .templates import db, GameState
from .ants import Ant


class Colony(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    species = db.Column(db.String(32))
    nests = db.relationship('Nest', backref='colony')
    ants = db.relationship('Ant', backref='colony')

    def __init__(self, world_id, user_id):
        self.world_id = world_id
        self.user_id = user_id
        self.species = 'black'

    def move_ants(self):
        for ant in self.ants:
            ant.perform_action()

    def birth_ant(self, x_pos=0, y_pos=0, role='basic'):
        ant_role_mapper = {
            'basic': Ant(colony_id=self.id, x_pos=10, y_pos=10),
            }
        self.ants.append(ant_role_mapper[role])

    def kill_ant(self, ant):
        pass

