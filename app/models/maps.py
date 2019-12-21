import sqlalchemy.orm.exc
import sqlalchemy.exc

from .templates import db, Template


class Map(Template):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    """Which world the colony belongs to."""

    x = db.Column(db.Integer, primary_key=True, nullable=False)
    """The x-coordinate location to look up."""

    y = db.Column(db.Integer, primary_key=True, nullable=False)
    """The y-coordinate location to look up."""

    ref_class = db.Column(db.String(30))
    """The Object type that lives at these coordinates."""

    ref_id = db.Column(db.Integer())
    """The Object id that lives at these coordinates."""

    def __init__(self, world_id, x, y, ref_class):
        self.world_id = world_id
        self.x = x
        self.y = y
        self.ref_class = ref_class

    def get_real_object(self):
        """Looks up the actual Object in the database from the reference Object type and id.

        Returns:
            Object: The object mapped to the coordinates.
        """
        return eval(f'{self.ref_class}.query.get({self.ref_id})')

    @classmethod
    def get_object_at_location(cls, x, y):
        """Looks up if an object exists at a location in the mapping.

        Args:
            x (int): The x-coordinate location to look up.
            y (int): The y-coordinate location to look up.

        Returns:
            Object: The object mapped to the coordinates. Otherwise None.
        """
        object_map_at_target_location = cls.query\
            .filter_by(x=x, y=y).one_or_none()
        if not object_map_at_target_location:
            return None
        return object_map_at_target_location.get_real_object()

    @staticmethod
    def add_object(world_id, object_to_be_added):
        """Creates a new mapping for an object.

        Args:
            world_id (int): Which world to map the object to.
            object_to_be_added (Object): The actual object to be mapped.

        Returns:
            new_mapping: The new mapping for the object. Otherwise None.
        """
        try:
            new_mapping = Map(world_id,
                              object_to_be_added.x,
                              object_to_be_added.y,
                              object_to_be_added.__class__.__name__)
            new_mapping.save()
            return new_mapping
        except (sqlalchemy.orm.exc.FlushError, sqlalchemy.exc.IntegrityError) as e:
            return None

    @classmethod
    def remove_object(cls, object_to_be_removed):
        """Removes a mapping for an object.

        Args:
            object_to_be_removed (Object): The Object to be removed from the world.
        """
        cls.query.filter_by(x=object_to_be_removed.x,
                            y=object_to_be_removed.y).delete()
