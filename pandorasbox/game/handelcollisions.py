import arcade
from game.action import Action
from game.constants import SCREEN_HEIGHT
from game.score import Score

class HandelCollisions(Action):

    def __init__(self, score: Score):
        self.score = score
        
    def arrow_hit_object(self, arrow_list, object_list, sound):
        for arrow in arrow_list:
            hit_objects = arcade.check_for_collision_with_list(arrow, object_list)
            for obj in hit_objects:
                obj.remove_from_sprite_lists() 
                arrow.remove_from_sprite_lists()
                arcade.play_sound(sound)

                # add points to score
                self.score.add_score()
                
    def arrow_off_screen(self, arrow_list):
        for arrow in arrow_list:
            if arrow.bottom > SCREEN_HEIGHT:
                arrow.remove_from_sprite_lists()
            
    def pandora_hit_object(self, player_list, object_list):
        if arcade.check_for_collision_with_list(player_list, object_list):
            player_list.remove_from_sprite_lists()
            return True
