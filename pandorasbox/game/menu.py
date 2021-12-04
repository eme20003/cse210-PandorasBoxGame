import arcade
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from game.instructions import InstructionView
from game.box import Box

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None

    def on_show(self):
        # background color
        arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.load_texture("cse210-PandorasBoxGame\pandorasbox\game\pb_images\ptreasure_chest.png")


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6,SCREEN_WIDTH/4, SCREEN_HEIGHT/4, self.background)
        arcade.draw_text("Pandora's Box", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 230, arcade.color.BLACK, font_size = 50, anchor_x = "center")
        arcade.draw_text("Pandora! Pandora. Pandora. Pandora. PANDORA! Pandora. Pandora!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.GRAY, font_size = 20, anchor_x = "center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 85, arcade.color.GRAY, font_size = 20, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)