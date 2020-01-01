import random

from .templates import db, GameState


class Ant(GameState):
    colony_id = db.Column(db.Integer, db.ForeignKey('colony.id'), nullable=False)
    """Which colony the ant belongs to."""

    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    """Which world the ant belongs to."""

    x = db.Column(db.Integer)
    """The x-coordinate location it's currently at."""

    y = db.Column(db.Integer)
    """The y-coordinate location it's currently at."""

    size = db.Column(db.Integer)
    """How much space the ant takes up when rendered."""

    caste = db.Column(db.String(20))
    """What type of ant it is."""

    __mapper_args__ = {'polymorphic_on': caste,
                       'polymorphic_identity': 'worker'}
    """Set the base class and the default identity of this class. Used for child classes
    that will inherit but live in the same database table."""

    carrying = db.Column(db.Boolean)
    """Whether or not the ant is carrying an object."""

    task = db.Column(db.String(20))
    """The current task the ant wants to perform."""

    is_releasing_pheromone = db.Column(db.Boolean)
    """Whether or not the ant is currently releasing a trail."""

    def __init__(self, colony_id, x, y):
        self.world_id = 1
        self.colony_id = colony_id
        self.x = x
        self.y = y
        self.size = 1
        self.caste = 'worker'
        self.carrying = False
        self.task = 'pass'

    def is_friendly(self, other_object):
        """Whether or not the ant is friendly towards another object.

        Args:
            other_object (Object): The other object which is interacting with this ant.

        Returns:
            Boolean: True if it is friendly. Otherwise False.
        """
        if self.colony_id == other_object.colony_id:
            return True
        return False

    def get_new_task(self):
        """Assigns this ant a new task to perform."""
        new_tasks = ['scout', 'feed', 'pass']
        weights = []
        for item in new_tasks:
            if item == self.colony.goal:
                weights.append(10)
            else:
                weights.append(1)
        self.task = random.choices(new_tasks, weights=weights)[0]

    def perform_action(self):
        """Forces the ant to perform its currently assigned task. If complete, it gets a new assignment."""
        ant_action_mapper = {'pass': self.sit_idle,
                             'scout': self.find_food,
                             'feed': self.find_food}
        action_completed = ant_action_mapper[self.task]()
        if action_completed:
            self.get_new_task()

    def sit_idle(self):
        """Forces the ant to do nothing.

        Returns:
            Boolean: Always True.
        """
        return True

    def move(self, x, y):
        """Forces the ant to attempt to move to a new location.

        Args:
            x (int): The x-coordinates of the new target.
            y (int): The y-coordinates of the new target.

        Returns:
            Boolean: Always returns True. ie. tells the Ant to get a new task.
            """
        # assert (self.x != x and self.y != y), "Ant trying to move nowhere"
        if (self.x == x and self.y == y):
            return False
        object_at_location = self.world.get_object_at_location(x=x, y=y)

        if hasattr(object_at_location, 'consumable') and object_at_location.consumable:
            """If it's a piece of food, move onto it."""
            self.eat(object_at_location)
            object_at_location.consumed()
            self.x, self.y = x, y
        elif hasattr(object_at_location, 'attackable') and object_at_location.attackable:
            """If it's an enemy ant, kill it."""
            if not self.is_friendly(object_at_location):
                self.attack(object_at_location)
                object_at_location.attack(self)
        elif object_at_location is None:
            """If it's an empty space, simply move there."""
            self.world.add_pheromone_trail(self.colony_id, self.x, self.y, x, y)
            self.x, self.y = x, y
        return True

    def temp_get_random_move_location(self):
        possible_x_coordinates = []
        possible_y_coordinates = []
        for i in range(-1, 2):
            if 0 <= self.x + i <= self.world.width:
                possible_x_coordinates.append(self.x + i)
            if 0 <= self.y + i <= self.world.height:
                possible_y_coordinates.append(self.y + i)
        x = random.choice(possible_x_coordinates)
        y = random.choice(possible_y_coordinates)
        return x,y

    def eat(self, food):
        """ Forces the ant to eat food.

        Args:
            food (Food Object): The food to be eaten.
        """
        self.colony.food_reserves += 1

    def attack(self, ant):
        """Forces the ant to attack another ant.

        Args:
            ant (Ant Object): The other ant to be attacked.
        """
        self.query.delete()

    def find_food(self):
        """Forces the ant to look for food."""
        x,y = self.temp_get_random_move_location()
        self.move(x, y)


class QueenAnt(Ant):
    __mapper_args__ = {'polymorphic_identity': 'queen'}

    def __init__(self, colony_id, x, y):
        super().__init__(colony_id, x, y)
        self.size = 5
        self.caste = 'queen'
        self.task = 'pass'

    def get_new_task(self):
        """Assigns this ant a new task to perform."""
        new_tasks = ['pass']
        weights = []
        for item in new_tasks:
            if item == self.colony.goal:
                weights.append(10)
            else:
                weights.append(1)
        self.task = random.choices(new_tasks, weights=weights)[0]

    def perform_action(self):
        """Forces the ant to perform its currently assigned task. If complete, it gets a new assignment."""
        ant_action_mapper = {'pass': self.sit_idle}
        action_completed = ant_action_mapper[self.task]()
        if action_completed:
            self.get_new_task()


class SoldierAnt(Ant):
    __mapper_args__ = {'polymorphic_identity': 'soldier'}

    def __init__(self, colony_id, x, y):
        super().__init__(colony_id, x, y)
        self.size = 5
        self.caste = 'soldier'
        self.task = 'scout'
