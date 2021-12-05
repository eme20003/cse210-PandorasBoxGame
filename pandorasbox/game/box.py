import arcade
from game.constants import SCALE_BOX, SCREEN_WIDTH

# Box Sprite
class Box(arcade.Sprite):
    """Box emits all the evils of the world. Inherits from arcade.Sprite

    Stereotype:
        Information Holder

    Attributes:
        arcade.Sprite: An instance of arcade.Sprite class
    """
    def __init__(self):
        super().__init__("pandorasbox\game\pb_images\ptreasure_chest.png", SCALE_BOX)
        self.top = 600
        self.center_x = SCREEN_WIDTH / 2

    def update(self):
        """"""
