class AntSerializer:
    def __init__(self):
        pass

    @classmethod
    def render(cls, ant):
        return dict(
            id=ant.id,
            pos=[ant.x_pos, ant.y_pos],
            size=ant.size,
            carrying=ant.carrying,
            caste=ant.caste,
            task=ant.task
        )
