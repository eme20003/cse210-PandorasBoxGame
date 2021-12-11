import arcade
from game.director import Director
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from game.menu import MenuView


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pandora's Box")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
