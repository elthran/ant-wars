class AntSerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, ant):
        # consider build a function that does
        # {attribute: getattr(ant, attribute) for attribute in ['id', 'x', 'y', 'size', ...]}
        # and move it into the Serializer superclass so you just do
        # return mapped_attributes??(['id', 'x', 'y', 'size', ...])
        return dict(
            id=ant.id,
            x=ant.x,
            y=ant.y,
            size=ant.size,
            carrying=ant.carrying,
            caste=ant.caste,
            task=ant.task
        )
