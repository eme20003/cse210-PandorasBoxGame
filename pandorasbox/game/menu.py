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
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6, SCREEN_WIDTH/4, SCREEN_HEIGHT/4, self.background)
        arcade.draw_text("Pandora's Box", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 230, arcade.color.BLACK, font_size = 45, anchor_x = "center")
        arcade.draw_text("Pandora. . . . Pandora. . . .", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.GRAY, font_size = 10, anchor_x = "center")
        arcade.draw_text("Pandora, click on the box.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 180, arcade.color.GRAY, font_size = 12, anchor_x = "center")
        arcade.draw_text("Click on the box Pandora.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 155, arcade.color.GRAY, font_size = 14, anchor_x = "center")
        arcade.draw_text("We're trapped Pandora! Let us out!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 125, arcade.color.GRAY, font_size = 14, anchor_x = "center")
        arcade.draw_text("Pandora! Pandora, please!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 95, arcade.color.GRAY, font_size = 17, anchor_x = "center")
        arcade.draw_text("Please Pandora! Pandora! Pandora!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60, arcade.color.GRAY, font_size = 17, anchor_x = "center")
        arcade.draw_text("Pandora please save us! Let us out!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 35, arcade.color.GRAY, font_size = 14, anchor_x = "center")
        arcade.draw_text("Pandora! Pandora! Pandora please! Please!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 5, arcade.color.GRAY, font_size = 24, anchor_x = "center")
        
        arcade.draw_text("Pandora. . . . Pandora. . . . save us.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60, arcade.color.GRAY, font_size = 14, anchor_x = "center")
        arcade.draw_text("Please save us Pandora. Please!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 85, arcade.color.GRAY, font_size = 20, anchor_x = "center")
        arcade.draw_text("Let us out. Click the box.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 105, arcade.color.GRAY, font_size = 14, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        '''When selecting the mouse, move to show the instructions'''
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)