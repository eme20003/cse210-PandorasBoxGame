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
        self.background = arcade.load_texture('pandorasbox/game/pb_images/scene_scroll_paper.png')

    def on_draw(self):
        '''Explains to the user the story of the game and what needs to take place
        Args:
            self(InstructionView): an instance of InstructionView'''
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        

        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 190, arcade.color.BLACK, font_size = 43, anchor_x = "center", font_name = "garamond")
        arcade.draw_text("OH NO!!! WHAT HAVE YOU DONE??!!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, arcade.color.BLACK, font_size = 22, anchor_x = "center", font_name = "candara")
        arcade.draw_text("By clicking on Pandora's box, you have unleashed a myriad of horrors which will afflict mankind!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 125, arcade.color.BLACK, font_size = 14, anchor_x = "center", font_name = "candara")
        arcade.draw_text("It is up to YOU to fix what YOU broke in the first place and save the world that YOU put in jeopardy!!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 105, arcade.color.BLACK, font_size = 13, anchor_x = "center", font_name = "candara") 
        
        arcade.draw_text("Shoot your arrows at plagues, monsters, hunger, emotional stresses like when Pluto was a planet, ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 65, arcade.color.BLACK, font_size = 13, anchor_x = "center", font_name = "candara")
        arcade.draw_text("then a mass of rocks, then a planet, then a star, money you see on the ground that turns out to be gum, ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 45, arcade.color.BLACK, font_size = 13, anchor_x = "center", font_name = "candara") 
        arcade.draw_text("homework, and other life-threatening items as they hurtle at your face!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 25, arcade.color.BLACK, font_size = 16, anchor_x = "center", font_name = "candara")
        
        arcade.draw_text("Eliminate these from existence and return the world to its state of progress-less, blissful ignorance ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 15, arcade.color.BLACK, font_size = 13, anchor_x = "center", font_name = "candara") 
        arcade.draw_text("where nothing good nor bad ever happens.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40, arcade.color.BLACK, font_size = 20, anchor_x = "center", font_name = "candara")

        arcade.draw_text(" SPACE BAR: shoot monsters", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80, arcade.color.BLACK_OLIVE, font_size = 13, anchor_x = "center", font_name = "candara")
        arcade.draw_text("<---  LEFT Arrow: move left", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 97, arcade.color.BLACK_OLIVE, font_size = 13, anchor_x = "center", font_name = "candara")
        arcade.draw_text(" --->  RIGHT Arrow: move right", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 114, arcade.color.BLACK_OLIVE, font_size = 13, anchor_x = "center", font_name = "candara")
        arcade.draw_text(" 3ish  LIVES: very unrealistic", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 131, arcade.color.BLACK_OLIVE, font_size = 13, anchor_x = "center", font_name = "candara")
        arcade.draw_text("Click again to begin saving the world from your dastardly deeds.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 171, arcade.color.GRAY, font_size = 22, anchor_x = "center", font_name = "garamond")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        '''Starts the game once the mouse button is pressed
        
        Args:
            self(InstructionView): an instance of InstructionView'''
        # Call to setup method in PandorasBox class
        director_view = Director()
        director_view.setup()
        self.window.show_view(director_view)
    
      