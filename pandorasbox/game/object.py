import arcade

# Objects coming from Pandora's Box
class Objects(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""