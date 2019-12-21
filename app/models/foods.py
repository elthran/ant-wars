from .templates import db, GameState
from .ants import Ant


class Food(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    """Which world the food belongs to."""

    x = db.Column(db.Integer())
    """The x-coordinate location it's currently at."""

    y = db.Column(db.Integer())
    """The y-coordinate location it's currently at."""

    value = db.Column(db.Integer())
    """How much food exists at this location."""

    def __init__(self, world_id, x, y, value=1):
        self.world_id = world_id
        self.x = x
        self.y = y
        self.value = value

    @property
    def consumable(self):
        """A property of edible objects.

        Returns:
            Boolean: True.
        """
        return True

    def consumed(self):
        """The food is diminished in value or removed."""
        self.value -= 1
        if self.value <= 0:
            self.world.remove_object(self)

