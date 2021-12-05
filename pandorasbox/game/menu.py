import arcade
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from game.instructions import InstructionView
from game.box import Box

class MenuView(arcade.View):
    def __init__(self):
        '''The Class contstructor
        
        Stereotype:
            Information Holder
        Attribute:
            arcade.View: An instance of the arcade.View class'''
        super().__init__()
        self.background = None

    def on_show(self):
        '''display the menu window'''
        # background color
        arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.load_texture("pandorasbox\game\pb_images\ptreasure_chest.png")


    def on_draw(self):
        '''Displays text on the background
        
        Args:
            self(MenuView): an instance of MenuView'''

        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6,SCREEN_WIDTH/4, SCREEN_HEIGHT/4, self.background)
        arcade.draw_text("Pandora's Box", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 230, arcade.color.BLACK, font_size = 50, anchor_x = "center")
        arcade.draw_text("Pandora! Pandora. Pandora. Pandora. PANDORA! Pandora. Pandora!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.GRAY, font_size = 20, anchor_x = "center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 85, arcade.color.GRAY, font_size = 20, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        '''When selecting the mouse, move to show the instructions'''
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)