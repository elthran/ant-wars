from templates import db, GameState
from tunnels import Tunnel


class Nest(GameState):
    colony_id = db.Column(db.Integer, db.ForeignKey('colony.id'), nullable=False)
    ants = db.relationship('Ant', backref='nest')
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    entrance_x_pos = db.Column(db.Integer)
    entrance_y_pos = db.Column(db.Integer)
    excavated_coordinates = db.relationship('Tunnels', backref='nest')

    def __init__(self, colony_id, width, height):
        self.colony_id = colony_id
        self.width = width
        self.height = height
        self.entrance_x_pos = width // 2
        self.entrance_y_pos = height - 1

    def get_colony(self):
        return

    def get_coordinates_of_all_tunnels(self):
        excavated_coordinates = []
        for tunnel in self.excavated_coordinates:
            excavated_coordinates.append((tunnel.x_pos, tunnel.y_pos))
        return self.excavated_coordinates

    def dig_tunnel(self, x, y):
        new_tunnel = Tunnel(self.id, x, y)
        new_tunnel.save()

    def get_coordinates_of_all_ants(self):
        ant_coordinates = []
        for ant in self.colony.ants:
            ant_coordinates.append((ant.x_pos, ant.y_pos))
        return ant_coordinates

    def __str__(self):
        s = ''
        for y_coordinate in range(self.height - 1, -1, -1):
            for x_coordinate in range(self.width):
                if (x_coordinate, y_coordinate) in self.get_coordinates_of_all_ants():
                    s += 'A'
                elif (x_coordinate, y_coordinate) in self.get_coordinates_of_all_tunnels():
                    s += '0'
                else:
                    s += 'X'
            s += '\n'
        return s
