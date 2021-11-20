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
SCALE_BOX = 1
SCALE_OBJECT = 1
SCALE_PANDORA = 1
SCALE_ARROW = 1

# bullet class
class Arrow(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# coin class
class Objects(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""


# pandora class
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

        # Player info
        self.player_sprite = None
        self.score = 0

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        """Setup the window. Allows you to refresh the screen
        instead of creating another instance."""

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()

        # add score
        self.score = 0

        # Player info
        self.pandora = Pandora(FILE, SCALE_PANDORA)
        self.player_sprite.bottom = 0
        self.player_sprite.left = 0

        # add pandora to the player list
        self.player_list.append(self.player_sprite)

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        """THIS IS ALWAYS NEEDED. OVERRIDES default method in parent class"""

        # prepare screen to draw
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()

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


        # Loop through each colliding sprite, remove it, and add to the score


arcade.finish_render()

if __name__ == "__main__":
    window = PandorasBox(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Call to setup method in PandorasBox class
    window.setup()
    arcade.run()
