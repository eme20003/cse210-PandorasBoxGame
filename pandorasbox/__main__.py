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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pandoras Box'

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.GRAY)
arcade.start_render()














arcade.finish_render()

if __name__ == "__main__":
    arcade.run()

