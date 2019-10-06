import random
import time


class World:
    # This is the world map. Currently unused since all game play takes place in a single nest for now.
    def __init__(self):
        self.colonies = []  # Each 'player' in the game

    def create_colony(self):
        next_id = len(self.colonies)
        new_colony = Colony(next_id)
        self.colonies.append(new_colony)


class Colony:
    # A new colony starts inside an empty 25x25 nest with a single ant.
    def __init__(self, id):
        self.id = id
        self.species = 'black'
        self.nest = Nest(id=0, colony=self, width=25, height=25)
        self.ants = []
        self.ant_id_counter = 0
        self.birth_ant()

    def move_ants(self):
        for ant in self.ants:
            ant.perform_action()

    def birth_ant(self, x_pos=0, y_pos=0, role='basic'):
        ant_role_mapper = {'basic': Ant(colony_id=self.id, id=self.ant_id_counter, nest=self.nest, x_pos=self.nest.width//2, y_pos=self.nest.height-1),
                           # 'worker': WorkerAnt(colony_id=self.id, id=self.ant_id_counter, nest=self.nest, x_pos=x_pos, y_pos=y_pos)
                           }
        self.ants.append(ant_role_mapper[role])
        self.ant_id_counter += 1

    def kill_ant(self, ant):
        pass


class Nest:
    def __init__(self, id, colony, width, height):
        self.id = id
        self.colony = colony
        self.width = width
        self.height = height
        self.entrance = (12, 24)
        self.excavated_coordinates = [self.entrance]

    def get_colony(self):
        return

    def get_coordinates_of_all_tunnels(self):
        return self.excavated_coordinates

    def dig_tunnel(self, x, y):
        self.excavated_coordinates.append((x, y))

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


class Ant:
    def __init__(self, colony_id, id, nest, x_pos, y_pos):
        self.colony_id = colony_id
        self.id = id
        self.nest = nest
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = 5
        self.actions = ['pass', 'move', 'dig']
        self.ant_action_mapper = {'pass': self.sit_idle(),
                                  'move': self.move(),
                                  'dig': self.dig()}

    def perform_action(self):
        action = random.choice(self.actions)
        print("Ant{id} is at position ({x},{y}) and is performing {action}".format(id=self.id,
                                                                                   x=self.x_pos,
                                                                                   y=self.y_pos,
                                                                                   action=action))
        try:
            print("Attempting to:", action)
            self.ant_action_mapper[action]
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


# class WorkerAnt:
#     def __init__(self, colony_id, id, nest, x_pos, y_pos):
#         super(WorkerAnt, self).__init__(colony_id, id, nest, x_pos, y_pos)
#         self.actions = ['pass', 'move', 'dig']


def run_game():
    # Initialize
    frame = 1
    game = World()
    game.create_colony()
    while True:
        print("Frame {frame}".format(frame=frame))
        print(game.colonies[0].nest)
        print("\n\n\n")
        game.colonies[0].move_ants()
        frame += 1
        if random.randint(1, 100) > 100:
            game.colonies[0].birth_ant()
        time.sleep(2)


run_game()
