import arcade
import random
from game.constants import(SCALE_OBJECT)
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Objects coming from Pandora's Box
class Objects(arcade.Sprite):
    """Evil objects released from Pandora's Box. 
    Inherits from arcade.Sprite

    Stereotype:
        Information Holder

    Attributes:
        arcade.Sprite: An instance of arcade.Sprite class
    """
    def __init__(self):
        super().__init__('cse210-PandorasBoxGame\pandorasbox\game\pb_images\monster2_blue.png', SCALE_OBJECT)
        
        self.velocity_X = random.randint(-4,4)
        self.velocity_Y = random.randint(-4, -2)
        self.change_x = 0
        self.change_y = 0
        

    def update(self):
        """"""
        
        self.center_y += self.velocity_Y
        self.center_x += self.velocity_X

        if self.left < 0:
            self.velocity_X *= -1

        if self.right > SCREEN_WIDTH:
            self.velocity_X *= -1

        if self.bottom < 0:
            self.velocity_Y *= -1

        if self.top > SCREEN_HEIGHT:
            self.velocity_Y *= -1
    