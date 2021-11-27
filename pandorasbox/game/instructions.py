import arcade
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from game.director import Director

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, font_size = 50, anchor_x = "center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75, arcade.color.GRAY, font_size = 20, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Call to setup method in PandorasBox class
        director_view = Director()
        director_view.setup(self)
        self.window.show_view(director_view)
    
      