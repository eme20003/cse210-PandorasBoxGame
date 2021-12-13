import sys
from game.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from game.pandora import Pandora
from game.box import Box
from game.arrow import Arrow
from game.object import Objects
from game.game_over import GameOverView
from game.handelcollisions import HandelCollisions
from game.score import Score
from game.health import Health
import random
import arcade


# Main Window
class Director(arcade.View):
    """ A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        arcade.Window: Instance of Window Class
    """
    def __init__(self):
        super().__init__()
        self.time_taken = 0

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.box_list = None

        self.score = Score()
        self.collisions = HandelCollisions(self.score)

        # Player info
        self.pandora = None

        # Box info
        self.box = None

        self.background = None

        # Sounds
        self.arrow_sound = arcade.load_sound('pandorasbox/game/pb_sounds/warfare_medieval_scythian_recurve_arrow_heavy_pass_by_002.mp3')
        self.blowup_sound = arcade.load_sound('pandorasbox/game/pb_sounds/zapsplat_explosion_med_large_71697.mp3')

        # Health bar
        self.health = None

    def setup(self):
        """Setup the window. Allows you to refresh the screen
        instead of creating another instance."""
        
        self.background = arcade.load_texture('pandorasbox/game/pb_images/scene_greek_town.png')

        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.object_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.level = ['one']

        # Player info
        self.pandora = Pandora()

        self.box = Box()

        self.object = Objects()
        self.object.top = 600
        self.object.center_x = (SCREEN_WIDTH / 2)

        # add pandora to the player list
        self.player_list.append(self.pandora)
        self.box_list.append(self.box)
        self.object_list.append(self.object)

        # background color
        arcade.set_background_color(arcade.color.GRAY)

        # Health Bar
        self.health = Health()
    
    
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
        output = f"Score: {self.score.get_score()}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 16)

        # draw the healthbar
        self.health.draw_bar()

    def on_update(self, delta_time):
        """Movement and game logic. THIS IS AUTOMATICALLY CALLED.
        Refresh rate is 60 Hz"""

        self.time_taken += delta_time

        # update all the sprites
        self.player_list.update()
        self.object_list.update()
        self.arrow_list.update()
        
        # Create a collision list        
        self.collisions.arrow_hit_object(self.arrow_list, self.object_list, self.blowup_sound)
        self.collisions.arrow_off_screen(self.arrow_list)
        

        if self.collisions.pandora_hit_object(self.player_list, self.object_list):
            if self.health.has_health():
                self.health.subtract()
            else:                            
                # display game over view
                game_over_view = GameOverView()
                game_over_view.score = self.score.get_score()
                game_over_view.time_taken = self.time_taken
                self.window.show_view(game_over_view)
                
        if len(self.object_list) == 0:
                
                self.level.append('one')
                for X in self.level:
                    self.object = Objects()
                    self.object.top = 600
                    self.object.center_x = random.randint(100, 700)
                    self.object_list.append(self.object)
            
        # update health bar
        self.health.draw_bar()

    def on_key_press(self, key, modifiers):
        """Method for moving Pandora left and right.
        Also fires arrows."""
        # Move using left or right arrow keys
        self.pandora.move_pandora(key)

        # Fire arrows with spacebar.
        if key == arcade.key.SPACE:
            self.arrow = Arrow(self.pandora)
            self.arrow_list.append(self.arrow)
            arcade.play_sound(self.arrow_sound)
            

    def on_key_release(self, key, modifiers):
        """Resets the movement to 0."""
        if key == arcade.key.RIGHT:
            self.pandora.change_x = 0
        if key == arcade.key.LEFT:
            self.pandora.change_x = 0