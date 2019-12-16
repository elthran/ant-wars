from .ant_serializer import AntSerializer


class ColonySerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, colony):
        nest_entrance = None
        for nest in colony.nests:
            nest_entrance = nest.entrance_x, nest.entrance_y
        return dict(
            id=colony.id,
            goal=colony.goal,
            username=colony.user.username,
            ants=[AntSerializer.render(ant) for ant in colony.ants],
            nest_entrance=nest_entrance,
            food_reserves=colony.food_reserves
        )
