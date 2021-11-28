import arcade

# Box Sprite
class Box(arcade.Sprite):
    """Box emits all the evils of the world. Inherits from arcade.Sprite

    Stereotype:
        Information Holder

    Attributes:
        arcade.Sprite: An instance of arcade.Sprite class
    """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

    def update(self):
        """"""
