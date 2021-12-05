import arcade
from game.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)
from game.director import Director

class InstructionView(arcade.View):
    def __init__(self):
        '''The Class contstructor
        
        Stereotype:
            Information Holder
        Attribute:
            arcade.View: An instance of the arcade.View class'''
        super().__init__()
        self.background = None

    
    def on_show(self):
        '''Display the backround as one of the images stored in pb_images
        
        Args:
            self(InstructionView): an instance of InstructionView'''
        self.background = arcade.load_texture('pandorasbox\game\pb_images\scene_scroll_paper.png')

    def on_draw(self):
        '''Explains to the user the story of the game and what needs to take place
        Args:
            self(InstructionView): an instance of InstructionView'''
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        

        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 190, arcade.color.BLACK, font_size = 40, anchor_x = "center")
        arcade.draw_text("Pandora’s box has been opened! It is up to you to fix what you broke in the first place ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size = 14, anchor_x = "center") 
        arcade.draw_text("and save the world that you put in jeopardy! Shoot your arrows at plagues, monsters, hunger, ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 130, arcade.color.BLACK, font_size = 13, anchor_x = "center")
        arcade.draw_text("emotional stresses like when Pluto was a planet, then a mass of rocks, then a planet, then a star,", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 110, arcade.color.BLACK, font_size = 13, anchor_x = "center") 
        arcade.draw_text("homework, and other life-threatening items as they hurtle at your face!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90, arcade.color.BLACK, font_size = 15, anchor_x = "center")
        arcade.draw_text("Eliminate these from existence and return the world to its state of progress-less, blissful ignorance ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50, arcade.color.BLACK, font_size = 13, anchor_x = "center") 
        arcade.draw_text("where nothing good nor bad ever happens.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 25, arcade.color.BLACK, font_size = 20, anchor_x = "center")
        arcade.draw_text("Click to begin saving the world from your dastardly deeds.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.GRAY, font_size = 20, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        '''Starts the game once the mouse button is pressed
        
        Args:
            self(InstructionView): an instance of InstructionView'''
        # Call to setup method in PandorasBox class
        director_view = Director()
        director_view.setup()
        self.window.show_view(director_view)
    
      