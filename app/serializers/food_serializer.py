class FoodSerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, food):
        return dict(
            id=food.id,
            value=food.value,
            x=food.x,
            y=food.y,
        )
