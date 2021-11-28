import arcade

from game.constants import ARROW_SPEED
# Arrow Sprite
class Arrow(arcade.Sprite):
    """Arrows destroy the evils released from Pandora's Box. Inherits from arcade.Sprite

    Stereotype:
        Information Holder

    Attributes:
        arcade.Sprite: An instance of arcade.Sprite class
    """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""
        self.center_y += ARROW_SPEED

