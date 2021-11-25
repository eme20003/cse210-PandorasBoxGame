import arcade
from game.constants import SCREEN_WIDTH
# Pandora Sprite
class Pandora(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """"""
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Keep Pandora on the Screen
        if self.left < 0:
            self.left = 0

        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

