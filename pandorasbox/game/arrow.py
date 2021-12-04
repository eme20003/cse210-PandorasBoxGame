import arcade
from game.constants import ARROW_SPEED, SCALE_ARROW
from game.pandora import Pandora

# Arrow Sprite
class Arrow(arcade.Sprite):
    """Arrows destroy the evils released from Pandora's Box. Inherits from arcade.Sprite

    Stereotype:
        Information Holder

    Attributes:
        arcade.Sprite: An instance of arcade.Sprite class
    """
    def __init__(self, pandora: Pandora):
        super().__init__("pandorasbox\game\pb_images\Parrow_up1.png", SCALE_ARROW)
        
        self.center_x = pandora.center_x
        self.center_y = pandora.center_y + 50

    def update(self):
        """"""
        self.center_y += ARROW_SPEED

