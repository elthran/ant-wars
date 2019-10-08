import random

from templates import db, GameState


class Ant(GameState):
    colony_id = db.Column(db.Integer, db.ForeignKey('colony.id'), nullable=False)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'), nullable=False)
    x_pos = db.Column(db.Integer)
    y_pos = db.Column(db.Integer)
    size = db.Column(db.Integer)

    def __init__(self, colony_id, nest_id, x_pos, y_pos):
        self.colony_id = colony_id
        self.nest_id = nest_id
        self.x_pos = x_pos
        self.y_pos = width
        self.size = 5

    def perform_action(self):
        actions = ['pass', 'move', 'dig']
        ant_action_mapper = {'pass': self.sit_idle,
                             'move': self.move,
                             'dig': self.dig}
        action = random.choice(actions)
        print("Ant{id} is at position ({x},{y}) and is performing {action}".format(id=self.id,
                                                                                   x=self.x_pos,
                                                                                   y=self.y_pos,
                                                                                   action=action))
        try:
            print("Attempting to:", action)
            ant_action_mapper[action]()
        except:
            raise EnvironmentError("The ant has broken.")

    def sit_idle(self):
        pass

    def get_adjacent_locations(self):
        adjacent_locations, valid_x_pos, valid_y_pos = [], [self.x_pos], [self.y_pos]
        if self.x_pos < self.nest.width - 1:
            valid_x_pos += [self.x_pos + 1]
        if self.x_pos > 0:
            valid_x_pos += [self.x_pos - 1]
        if self.y_pos < self.nest.height - 1:
            valid_y_pos += [self.y_pos + 1]
        if self.y_pos < 0:
            valid_y_pos += [self.y_pos - 1]
        for x in valid_x_pos:
            for y in valid_y_pos:
                if x != self.x_pos or y != self.y_pos:
                    adjacent_locations.append((x, y))
        return adjacent_locations

    def move(self):
        list_of_all_possible_moves = self.get_adjacent_locations()
        list_of_all_possible_moves = [location for location in list_of_all_possible_moves if
                                      location in self.nest.get_coordinates_of_all_tunnels()]
        random.shuffle(list_of_all_possible_moves)
        for each in list_of_all_possible_moves:
            if each in self.nest.get_coordinates_of_all_tunnels():
                print("Was at:", self.x_pos, self.y_pos)
                self.x_pos, self.y_pos = each[0], each[1]
                print("Moved to:", self.x_pos, self.y_pos)
                break

    def dig(self):
        list_of_all_possible_moves = self.get_adjacent_locations()
        random.shuffle(list_of_all_possible_moves)
        for each in list_of_all_possible_moves:
            if each not in self.nest.get_coordinates_of_all_tunnels():
                print("Was at:", self.x_pos, self.y_pos)
                self.x_pos, self.y_pos = each[0], each[1]
                self.nest.dig_tunnel(each[0], each[1])
                print("Dug to:", self.x_pos, self.y_pos)
                break
