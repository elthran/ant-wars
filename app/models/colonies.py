from .templates import db, GameState
from .ants import Ant, QueenAnt
import random


class Colony(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    species = db.Column(db.String(32))
    nests = db.relationship('Nest', backref='colony')
    ants = db.relationship('Ant', backref='colony')
    goal = db.Column(db.String(20))
    food_reserves = db.Column(db.Integer())

    def __init__(self, world_id, user_id):
        self.world_id = world_id
        self.user_id = user_id
        self.species = 'black'
        self.goal = 'scout'
        self.food_reserves = 1

    @property
    def has_queen(self):
        for ant in self.ants:
            if ant.caste == 'queen':
                return True
        return False

    def update_goal(self, new_goal):
        if new_goal in ('scout', 'feed', 'pass'):
            self.goal = new_goal
        else:
            pass
        for ant in self.ants:
            ant.get_new_task()

    def advance_time(self):
        self.move_ants()
        if self.food_reserves > 0:
            self.birth_ant()
            self.food_reserves -= 1

    def move_ants(self):
        for ant in self.ants:
            ant.perform_action()

    def birth_ant(self, x=0, y=0, role='basic'):
        x, y = random.randint(0,20),random.randint(0,20)
        if len(self.nests) > 0:
            first_nest = self.nests[0]
            x, y = first_nest.entrance_x, first_nest.entrance_y
        ant_role_mapper = {
            'basic': Ant(colony_id=self.id, x=x, y=y),
            }
        new_ant = ant_role_mapper[role] if self.has_queen else QueenAnt(colony_id=self.id, x=x, y=y)
        self.world.add_object(new_ant)

    def kill_ant(self, ant):
        pass

