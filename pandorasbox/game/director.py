import sys
from time import sleep
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    #SCREEN_TITLE,
    SCALE_BOX,
    SCALE_OBJECT,
    SCALE_PANDORA,
    SCALE_ARROW,
    #ARROW_SPEED,
)
from game.pandora import Pandora
from game.box import Box
from game.arrow import Arrow
from game.object import Objects
import random
import arcade

# Main Window
class Director(arcade.Window):
    """ A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        arcade.Window: Instance of Window Class
    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.box_list = None

        # Player info
        self.pandora = None
        self.score = 0

        # Box info
        self.box = None

        self.background = None

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        """Setup the window. Allows you to refresh the screen
        instead of creating another instance."""

        self.background = arcade.load_texture('pandorasbox\game\pb_images\scene_greek_town.jpeg')

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.level = ['one']

        # add score
        self.score = 0

        # Player info
        self.pandora = Pandora("pandorasbox\game\pb_images\pandora_shoot_up.png", SCALE_PANDORA)
        self.pandora.bottom = 0
        self.pandora.center_x = SCREEN_WIDTH / 2

        self.box = Box("pandorasbox\game\pb_images\ptreasure_chest.png", SCALE_BOX)
        self.box.top = 600
        self.box.center_x = SCREEN_WIDTH / 2

        self.object = Objects('pandorasbox\game\pb_images\monster2_blue.jpg', SCALE_OBJECT)
        self.object.top = 600
        self.object.center_x = (SCREEN_WIDTH / 2)

        # add pandora to the player list
        self.player_list.append(self.pandora)
        self.box_list.append(self.box)
        self.object_list.append(self.object)

        # background color
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        """THIS IS ALWAYS NEEDED. OVERRIDES default method in parent class"""

        # prepare screen to draw
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw player lists
        self.player_list.draw()
        self.object_list.draw()
        self.arrow_list.draw()
        self.box_list.draw()

        # draw the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 16)

    def update(self, deltatime):
        """Movement and game logic. THIS IS AUTOMATICALLY CALLED.
        Refresh rate is 60 Hz"""

        # update all the sprites
        self.player_list.update()
        self.object_list.update()
        self.arrow_list.update()
        
        # Create a collision list
        
        for arrow in self.arrow_list:
            hit_objects = arcade.check_for_collision_with_list(arrow, self.object_list)
            for obj in hit_objects:
                self.score += int(10)
                obj.remove_from_sprite_lists()
                arrow.remove_from_sprite_lists()

            if self.arrow.bottom > SCREEN_HEIGHT:
                self.arrow.remove_from_sprite_lists()
            
            if arcade.check_for_collision_with_list(self.pandora, self.object_list):
                print(F'GAME OVER {self.score} POINTS')
                sys.exit()
                
        if len(self.object_list) == 0:
                
                self.level.append('one')
                for X in self.level:
                    self.object = Objects('pandorasbox\game\pb_images\monster2_blue.jpg', SCALE_OBJECT)
                    self.object.top = 600
                    self.object.center_x = random.randint(100, 700)
                    self.object_list.append(self.object)
                
                
            

            


    def on_key_press(self, key, modifiers):
        """Method for moving Pandora left and right.
        Also fires arrows."""
        
        # Move using left or right arrow keys
        if key == arcade.key.RIGHT:
            self.pandora.change_x = 6
        if key == arcade.key.LEFT:
            self.pandora.change_x = -6

        # Fire arrows with spacebar.
        if key == arcade.key.SPACE:
            self.arrow = Arrow("pandorasbox\game\pb_images\Parrow_up1.png", SCALE_ARROW)
            self.arrow.center_x = self.pandora.center_x
            self.arrow.center_y = self.pandora.center_y + 50
            self.arrow_list.append(self.arrow)

    def on_key_release(self, key, modifiers):
        """Resets the movement to 0."""
        if key == arcade.key.RIGHT:
            self.pandora.change_x = 0
        if key == arcade.key.LEFT:
            self.pandora.change_x = 0