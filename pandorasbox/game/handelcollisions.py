import arcade
from game.action import Action
from game.constants import SCREEN_HEIGHT
from game.score import Score
from arcade import SpriteList, Sprite

class HandelCollisions(Action):

    def __init__(self, score: Score):
        '''The Class Constructor
        
            Stereotype:
                Information Holder
                
            Attribute:
               score: an instance of score'''
        self.score = score
        
    def arrow_hit_object(self, arrow_list: SpriteList, object_list: SpriteList, sound):
        '''When the arrow hits an object (or in this instance a monster) 
        will remove the arrow from the arrows already shot, and will remove the 
        object or monster hit.  This will also make the exploding sound and add a 
        score to the players points
        
        Args: self(HandleCollisions): is an instance of HandleCollisions
        arrow_list(list): the arrows shot
        object_list(list): the enemies on the screen
        sound(file): the sound the arrow makes'''
        for arrow in arrow_list:
            hit_objects = arcade.check_for_collision_with_list(arrow, object_list)
            for obj in hit_objects:
                obj.remove_from_sprite_lists() 
                arrow.remove_from_sprite_lists()
                arcade.play_sound(sound)

                # add points to score
                self.score.add_score()
                
    def arrow_off_screen(self, arrow_list: SpriteList):
        '''If the arrow moves off the screen, remove the arrow
        Args:
        arrow_list(list): the arrows shot'''
        for arrow in arrow_list:
            if arrow.bottom > SCREEN_HEIGHT:
                arrow.remove_from_sprite_lists()
            
    def pandora_hit_object(self, player_list: SpriteList, object_list: SpriteList):
        '''If the player is hit by an object or monster remove the player from the screen
        
        Args:
        
        object_list(list): the enemies on the screen'''
        for player in player_list:
            hit_objects = arcade.check_for_collision_with_list(player, object_list)
            for obj in hit_objects:
                obj.remove_from_sprite_lists()            
                return True
            else:
                return False
