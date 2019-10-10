from .templates import db, GameState
from .ants import Ant


class Colony(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    species = db.Column(db.String(32))
    nests = db.relationship('Nest', backref='colony')
    ants = db.relationship('Ant', backref='colony')

    def __init__(self, world_id):
        self.world_id = world_id
        self.species = 'black'

    def move_ants(self):
        for ant in self.ants:
            ant.perform_action()

    def birth_ant(self, x_pos=0, y_pos=0, role='basic'):
        ant_role_mapper = {
            'basic': Ant(colony_id=self.id, id=self.ant_id_counter, nest=self.nest, x_pos=self.nest.width // 2,
                         y_pos=self.nest.height - 1),
            # 'worker': WorkerAnt(colony_id=self.id, id=self.ant_id_counter, nest=self.nest, x_pos=x_pos, y_pos=y_pos)
            }
        self.ants.append(ant_role_mapper[role])
        self.ant_id_counter += 1

    def kill_ant(self, ant):
        pass
