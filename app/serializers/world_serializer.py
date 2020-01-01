from .colony_serializer import ColonySerializer
from .food_serializer import FoodSerializer


class WorldSerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, world):
        return dict(
            id=world.id,
            age=world.age,
            colonies=[ColonySerializer.render(colony) for colony in world.colonies],
            foods=[FoodSerializer.render(food) for food in world.foods]
        )
