import arcade

from game.constants import ARROW_SPEED
# Arrow Sprite
class Arrow(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""
        self.center_y += ARROW_SPEED

