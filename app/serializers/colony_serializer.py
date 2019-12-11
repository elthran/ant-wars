from .ant_serializer import AntSerializer


class ColonySerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, colony):
        nest_entrance = None
        for nest in colony.nests:
            nest_entrance = nest.entrance_x_pos, nest.entrance_y_pos
        return dict(
            id=colony.id,
            goal=colony.goal,
            user_id=colony.user_id,
            ants=[AntSerializer.render(ant) for ant in colony.ants],
            nest_entrance=nest_entrance
        )
