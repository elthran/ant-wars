import sqlalchemy.orm.exc
import sqlalchemy.exc

from .templates import db, GameState, Template
from .ants import Ant
from .foods import Food


class Map(Template):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    x_pos = db.Column(db.Integer, primary_key=True, nullable=False)
    y_pos = db.Column(db.Integer, primary_key=True, nullable=False)
    ref_class = db.Column(db.String(30))
    ref_id = db.Column(db.Integer())

    def __init__(self, world_id, x_pos, y_pos, ref_class):
        self.world_id = world_id
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ref_class = ref_class

    def get_real_object(self):
        print("IS THIS THE ERROR?!?!:", f'{self.ref_class}.query.get({self.ref_id})')
        return eval(f'{self.ref_class}.query.get({self.ref_id})')

    @classmethod
    def get_object_at_location(cls, x_pos, y_pos):
        """
        Before an object moves, it should request to see what exists in the new location.
        """
        object_map_at_target_location = cls.query\
            .filter_by(x_pos=x_pos, y_pos=y_pos).one_or_none()
        if not object_map_at_target_location:
            return None
        return object_map_at_target_location.get_real_object()

    @staticmethod
    def add_object(world_id, object_to_be_added):
        try:
            new_mapping = Map(world_id,
                              object_to_be_added.x_pos,
                              object_to_be_added.y_pos,
                              object_to_be_added.__class__.__name__)
            new_mapping.save()
            return new_mapping
        except (sqlalchemy.orm.exc.FlushError, sqlalchemy.exc.IntegrityError) as e:
            return None

    @classmethod
    def remove_object(cls, object_to_be_removed):
        cls.query.filter_by(x_pos=object_to_be_removed.x_pos,
                            y_pos=object_to_be_removed.y_pos).delete()
