import arcade
from game.director import Director
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
)
from game.menu import MenuView


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pandora's Box")
    menu_view = MenuView()
    window.show_view(menu_view)
    
    # window = Director(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    #Things I added that I hope will help
    # window.total_score = 0

    # Call to setup method in PandorasBox class
    # window.setup()

    # Run arcade
    arcade.run()
