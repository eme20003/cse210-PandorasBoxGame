import arcade
from game.constants import SCREEN_WIDTH, SCALE_PANDORA
# Pandora Sprite
class Pandora(arcade.Sprite):
    def __init__(self):
        super().__init__("pandorasbox\game\pb_images\pandora_shoot_up.png", SCALE_PANDORA)
        self.bottom = 0
        self.center_x = SCREEN_WIDTH / 2
        self.change_x = 0

    def update(self):
        """"""
        self.center_x += self.change_x

        # Keep Pandora on the Screen
        if self.left < 0:
            self.left = 0

        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

    def move_pandora(self, key):
        if key == arcade.key.RIGHT:  
            self.change_x = 6
        if key == arcade.key.LEFT:
            self.change_x = -6