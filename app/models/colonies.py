from .templates import db, GameState
from .ants import Ant, QueenAnt, SoldierAnt
import random


class Colony(GameState):
    """A 'player' in the game."""

    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    """Which world the colony belongs to."""

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    """Which user the colony belongs to."""

    species = db.Column(db.String(32))
    """Which species of ant the colony is."""

    nests = db.relationship('Nest', backref='colony')
    """All nests that belong to this colony."""

    ants = db.relationship('Ant', backref='colony')
    """All ants that belong to this colony."""

    goal = db.Column(db.String(20))
    """The current object of the colony which directs how the ants will behave."""

    food_reserves = db.Column(db.Integer())
    """The amount of food the colony has saved up."""

    def __init__(self, world_id, user_id):
        self.world_id = world_id
        self.user_id = user_id
        self.species = 'black'
        self.goal = 'scout'
        self.food_reserves = 10

    @property
    def has_queen(self):
        """Checks if the colony currently has a queen.

        Returns:
            Boolean: True if this colony has a queen.
        """
        for ant in self.ants:
            if ant.caste == 'queen':
                return True
        return False

    def update_goal(self, new_goal):
        """Changes the current goal of the colony.

        Args:
            new_goal (str): The new goal.
        """
        if new_goal in ('scout', 'feed', 'pass'):
            self.goal = new_goal
        else:
            pass
        for ant in self.ants:
            ant.get_new_task()

    def advance_time(self):
        """Moves everything in the colony when time progresses."""
        self.move_ants()
        if self.food_reserves > 0:
            self.birth_ant()
            self.food_reserves -= 1

    def move_ants(self):
        """Tells each ant to move when time progresses."""
        for ant in self.ants:
            ant.perform_action()

    def birth_ant(self, x=0, y=0, role='basic'):
        """Tries to create a new ant if conditions are met.

        Args:
            x (int): The x-coordinate of where to place the new ant.
            y (int): The y-coordinate of where to place the new ant.
            role (str): What type of ant to birth.
        """
        x, y = random.randint(0,20),random.randint(0,20)
        if len(self.nests) > 0:
            first_nest = self.nests[0]
            x, y = first_nest.entrance_x, first_nest.entrance_y
        ant_role_mapper = {
            'basic': Ant(colony_id=self.id, x=x, y=y),
            'soldier': SoldierAnt(colony_id=self.id, x=x, y=y),
            }
        new_ant = ant_role_mapper[role] if self.has_queen else QueenAnt(colony_id=self.id, x=x, y=y)
        self.world.add_object(new_ant)

