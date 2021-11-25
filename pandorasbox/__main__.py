import arcade
from game.director import Director
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
)

if __name__ == "__main__":
    window = Director(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Call to setup method in PandorasBox class
    window.setup()

    # Run arcade
    arcade.run()
