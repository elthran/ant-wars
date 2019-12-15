from .templates import db, GameState
from .ants import Ant
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

    def birth_ant(self, x_pos=0, y_pos=0, role='basic'):
        x_pos, y_pos = random.randint(0,20),random.randint(0,20)
        if len(self.nests) > 0:
            first_nest = self.nests[0]
            x_pos, y_pos = first_nest.entrance_x_pos, first_nest.entrance_y_pos
        ant_role_mapper = {
            'basic': Ant(colony_id=self.id, x_pos=x_pos, y_pos=y_pos),
            }
        new_ant = ant_role_mapper[role]
        new_ant.save()
        self.world.add_object(new_ant)

    def kill_ant(self, ant):
        pass

