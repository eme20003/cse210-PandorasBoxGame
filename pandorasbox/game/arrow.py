import arcade

from game.constants import ARROW_SPEED, SCALE_ARROW
# Arrow Sprite
class Arrow(arcade.Sprite):
    """Arrows destroy the evils released from Pandora's Box. Inherits from arcade.Sprite

    Stereotype:
        Information Holder

    Attributes:
        arcade.Sprite: An instance of arcade.Sprite class
    """
    def __init__(self):
        super().__init__("pandorasbox\game\pb_images\Parrow_up1.png", SCALE_ARROW)

    def update(self):
        """"""
        self.center_y += ARROW_SPEED

