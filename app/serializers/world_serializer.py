from .colony_serializer import ColonySerializer


class WorldSerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, world):
        return dict(
            id=world.id,
            colonies=[ColonySerializer.render(colony) for colony in world.colonies]
        )
