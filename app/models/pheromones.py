from .templates import db, Template

import sqlalchemy.orm.exc
import sqlalchemy.exc


class Pheromone(Template):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    """Which world the colony belongs to."""

    colony_id = db.Column(db.Integer, primary_key=True, nullable=False)
    """The colony id that lives at these coordinates."""

    x = db.Column(db.Integer, primary_key=True, nullable=False)
    """The x-coordinate location to look up."""

    y = db.Column(db.Integer, primary_key=True, nullable=False)
    """The y-coordinate location to look up."""

    function = db.Column(db.String(30))
    """The purpose of the scent."""

    degrees = db.Column(db.Integer)
    """A number between 0 to 359 inclusive with 0 being due north and 90 being due east. 
    It points where the ant came from."""

    strength = db.Column(db.Integer)
    """The strength of the scent. It diminishes with age."""

    def __init__(self, world_id, colony_id, x, y, function, degrees, strength):
        self.world_id = world_id
        self.colony_id = colony_id
        self.x = x
        self.y = y
        self.function = function
        self.degrees = degrees
        self.strength = strength

    @staticmethod
    def add_pheromone(world_id, colony_id, x, y, function, degrees, strength):
        try:
            new_pheromone = Pheromone(world_id, colony_id, x, y, function, degrees, strength)
            new_pheromone.save()
            return new_pheromone
        except (sqlalchemy.orm.exc.FlushError, sqlalchemy.exc.IntegrityError) as e:
            db.session.rollback()
            return None

    @classmethod
    def get_pheromone_functionality(cls, colony_id, x, y):
        pheromone = cls.query.filter_by(colony_id=colony_id, x=x, y=y).one_or_none()
        return pheromone.function
