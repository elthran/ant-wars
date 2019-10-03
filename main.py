import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class World(object):
    """
    The side-view 'map' of the ant's nest as a 2d co-ordinate system

    Args:
        width/height (int): The dimensions of the world . This is the smallest step an object can take
        ants (list of Ant objects): A list containing each Ant which exists within the game
        food_supply (list of Food objects): A list containing each food which exists within the game
    """

    def __init__(self):
        self.width = 100
        self.height = 100
        self.ants = [Ant(5, 5, self) for i in range(5)]
        self.food_supply = [Food() for i in range(100)]

    def check_if_coordinate_has_food(self, ant):
        """
        Check if an ant has stepped onto a piece of food. If true, update the food and ant objects

        :param ant: The ant object which may have reached food
        """
        uneaten_food = [food for food in self.food_supply if food.eaten is False]
        for food in uneaten_food:
            if (ant.x_pos - 1 <= food.x_pos <= ant.x_pos + 1) and (ant.y_pos - 1 <= food.y_pos <= ant.y_pos + 1):
                food.is_eaten()
                ant.eats_food()


class Food(object):
    """
    A piece of food that an Ant may eat.

    Args:
        x_pos/y_pos (int): The coordinates on the map that the Food is currently at
        eaten (boolean): Whether the food still exists
        image (plot point): How the food will be drawn by matplotlib
    """

    def __init__(self):
        self.x_pos = random.randint(1, 100)
        self.y_pos = random.randint(1, 100)
        self.eaten = False
        self.image = plt.Circle((self.x_pos, self.y_pos), 1, color='g', fill=True)

    def is_eaten(self):
        """
        This function runs when an Ant eats the food. It is marked as eaten and becomes invisible
        """
        self.eaten = True
        self.image.set_radius(0)


class Ant(object):
    """
    An Ant which exists on the map.

    Args:
        x_pos/y_pos (int): The coordinates on the map that the Ant is currently at
        velx/vely (boolean): The speed and direction that the Ant will move next
        size (int): How large the ant should be on the graph
        world (World object): Which world the Ant currently resides in
    """

    def __init__(self, x_pos, y_pos, world):
        self.x_pos = x_pos * np.random.random_sample()
        self.y_pos = y_pos * np.random.random_sample()
        self.velx = self.generate_new_velocity()
        self.vely = self.generate_new_velocity()
        self.size = 5
        self.world = world

    def eats_food(self):
        """
        This function runs when an Ant eats the food. It grows in size
        """
        self.size += 5

    @staticmethod
    def generate_new_velocity():
        """
        This function generates a new velocity for the Ant after each frame
        """
        return random.randint(0, 1)

    def check_if_found_food(self):
        """
        This function checks if the Ant found food
        """
        self.world.check_if_coordinate_has_food(self)

    def move(self):
        """
        This function gets a new random velocity and moves the ant, checking for food
        """
        if np.random.random_sample() < 0.95:
            self.x_pos = self.x_pos + self.velx
            self.y_pos = self.y_pos + self.vely
        else:
            self.velx = self.generate_new_velocity()
            self.vely = self.generate_new_velocity()
            self.x_pos = self.x_pos + self.velx
            self.y_pos = self.y_pos + self.vely
        if self.x_pos >= 100:
            self.x_pos = 100
            self.velx = -1 * self.velx
        if self.x_pos <= 0:
            self.x_pos = 0
            self.velx = -1 * self.velx
        if self.y_pos >= 100:
            self.y_pos = 100
            self.vely = -1 * self.vely
        if self.y_pos <= 0:
            self.y_pos = 0
            self.vely = -1 * self.vely
        self.check_if_found_food()


# Get the World object
world = World()
# Generate the plot-figure
plot_figure = plt.figure()
# Create the dimensions of the image based on the World size
world_axes = plt.axes(xlim=(0, world.width), ylim=(0, world.height))
# Plot all of the Ants as 'red' '+'-symbols
d, = world_axes.plot([ant.x_pos for ant in world.ants],
                     [ant.y_pos for ant in world.ants], 'r+')
# Draw all of the food images
for food in world.food_supply:
    world_axes.add_artist(food.image)


# Animate the ants. This is done sequentially.
def animate(i):
    """
    Move each Ant. Then re-draw each Ant after they have moved.
    """
    for ant in world.ants:
        ant.move()
    d.set_data([ant.x_pos for ant in world.ants],
               [ant.y_pos for ant in world.ants])
    return d,


# Run the animation function.
anim = animation.FuncAnimation(plot_figure, animate, frames=200, interval=20)
# Show all of the work we have plotted.
plt.show()
