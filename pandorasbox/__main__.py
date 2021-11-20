import random
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.action import Action
from game import constants
from game.controlactors import ControlActors
from game.handelcollisions import HandelCollisions
from game.inputservice import InputService
from game.moveactors import MoveActors
from game.outputservice import OutputService
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pandoras Box"

# Arrow Sprite
class Arrow(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# Box Sprite
class Box(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# Objects coming from Pandora's Box
class Objects(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# Pandora Sprite
class Pandora(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# Main Window
class PandorasBox(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.box_list = None

        # Player info
        self.pandora = None
        self.score = 0

        # Box info
        self.box = None

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        """Setup the window. Allows you to refresh the screen
        instead of creating another instance."""

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()

        # add score
        self.score = 0

        # Player info
        self.pandora = Pandora()
        self.pandora.bottom = 0
        self.pandora.left = 0

        # Box info
        self.box = Box()
        self.box.center_x = SCREEN_HEIGHT - 50
        self.box.center_y = SCREEN_WIDTH / 2

        # add pandora to the player list
        self.player_list.append(self.pandora)

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        """THIS IS ALWAYS NEEDED. OVERRIDES default method in parent class"""

        # prepare screen to draw
        arcade.start_render()

        # Draw player lists
        self.player_list.draw()
        self.object_list.draw()
        self.arrow_list.draw()
        self.box_list.draw()

        # draw the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)

    def update(self, deltatime):
        """Movement and game logic. THIS IS AUTOMATICALLY CALLED.
        Refresh rate is 60 Hz"""

        # update all the sprites
        self.player_list.update()
        self.object_list.update()
        self.arrow_list.update()

        # Create a collision list
        for arrow in self.arrow_list:
            hit_objects = arcade.check_for_collision_with_list(arrow, self.object_list)
            for obj in hit_objects:
                self.score += int(10)
                obj.remove_from_sprite_lists()
                arrow.remove_from_sprite_lists()


if __name__ == "__main__":
    window = PandorasBox(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Call to setup method in PandorasBox class
    window.setup()

    # Run arcade
    arcade.run()
