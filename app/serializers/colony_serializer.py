from .ant_serializer import AntSerializer


class ColonySerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, colony):
        return dict(
            id=colony.id,
            ants=[AntSerializer.render(ant) for ant in colony.ants]
        )
