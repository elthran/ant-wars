from .ant_serializer import AntSerializer


class ColonySerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, colony):
        return dict(
            id=colony.id,
            goal=colony.goal,
            username=colony.user.username,
            ants=[AntSerializer.render(ant) for ant in colony.ants],
            nest_entrance=[(nest.entrance_x, nest.entrance_y) for nest in colony.nests],
            food_reserves=colony.food_reserves
        )
