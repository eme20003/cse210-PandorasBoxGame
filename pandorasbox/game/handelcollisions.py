from os import remove
import sys
from game import constants
import arcade
from game.action import Action
from game.constants import SCREEN_HEIGHT

class HandelCollisions(Action):

    def __init__(self):
        arrow_list = arcade.SpriteList()
        object_list = arcade.SpriteList()
        player_list = arcade.SpriteList()
        
    def arrow_hit_object(self, arrow_list, object_list):
        for arrow in arrow_list:
            hit_objects = arcade.check_for_collision_with_list(arrow, object_list)
            for obj in hit_objects:
                obj.remove_from_sprite_lists() 
                arrow.remove_from_sprite_lists()
                arcade.play_sound(self.blowup_sound)
                
    def arrow_off_screen(self, arrow_list):
        for arrow in arrow_list:
            if self.arrow.bottom > SCREEN_HEIGHT:
                self.arrow.remove_from_sprite_lists()
            
    def pandora_hit_object(self, player_list):
        if arcade.check_for_collision_with_list(self.pandora, self.object_list):
            self.pandora.remove_from_sprite_lists()
            print('GAME OVER')
            sys.exit()