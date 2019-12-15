import random

from .templates import db, GameState


class Ant(GameState):
    colony_id = db.Column(db.Integer, db.ForeignKey('colony.id'), nullable=False)
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    x_pos = db.Column(db.Integer)
    y_pos = db.Column(db.Integer)
    size = db.Column(db.Integer)
    caste = db.Column(db.String(20))
    carrying = db.Column(db.Boolean)
    task = db.Column(db.String(20))

    def __init__(self, colony_id, x_pos, y_pos):
        self.world_id = 1
        self.colony_id = colony_id
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = 5
        self.caste = 'worker'
        self.carrying = False
        self.task = 'pass'

    def get_new_task(self):
        new_tasks = ['scout', 'feed', 'pass']
        weights = []
        for item in new_tasks:
            if item == self.colony.goal:
                weights.append(10)
            else:
                weights.append(1)
        self.task = random.choices(new_tasks, weights=weights)[0]

    def perform_action(self):
        """
        Perform an action and then get your newly assigned task.
        """
        ant_action_mapper = {'pass': self.sit_idle,
                             'scout': self.move,
                             'feed': self.find_food}
        action_completed = ant_action_mapper[self.task]()
        if action_completed:
            self.get_new_task()

    def sit_idle(self):
        return True

    def move(self):
        possible_x_coordinates = []
        possible_y_coordinates = []
        for i in range(-1, 2):
            if 0 <= self.x_pos + i <= self.world.width:
                possible_x_coordinates.append(self.x_pos + i)
            if 0 <= self.y_pos + i <= self.world.height:
                possible_y_coordinates.append(self.y_pos + i)
        new_x_pos = random.choice(possible_x_coordinates)
        new_y_pos = random.choice(possible_y_coordinates)

        object_at_location = self.world.move(old_x=self.x_pos,
                                             old_y=self.y_pos,
                                             new_x=new_x_pos,
                                             new_y=new_y_pos)

        if hasattr(object_at_location, 'eatable') and object_at_location.eatable:
            ant.eat(object_at_location)
            object_at_location.consumed()
        elif hasattr(object_at_location, 'attackable') and object_at_location.attackable:
            ant.attack(object_at_location)
            object_at_location.attack(ant)

    def eat(self, food):
        self.colony.food_reserves += 1

    def attack(self, ant):
        self.query.delete()

    def find_food(self):
        self.move()
